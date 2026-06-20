from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKS_DIR = ROOT / "packs"
HEADING_RE = re.compile(r"^##\s+(?P<name>[A-Z-]+)\s*$")
PAIR_ID_RE = re.compile(r"^(?P<prefix>[A-Z]+)-(?P<kind>[KX])(?P<number>\d+)$")
ROUTING_ID_RE = re.compile(r"^[RL]\d+$")
STAGE_ID_RE = re.compile(r"^S\d{2}$")
LOWER_SIGNAL_RE = re.compile(r"^[a-z0-9-]+$")
FAMILY_PREFIXES = {
    "universal": "UNI",
    "cpp-architecture": "CPP",
    "python-architecture": "PY",
}


@dataclass(frozen=True)
class Record:
    file_path: Path
    line_number: int
    section: str
    raw: str
    record_id: str
    fields: dict[str, str]


class LintState:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, line_number: int, message: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT)}:{line_number}: {message}")

    def warning(self, path: Path, line_number: int, message: str) -> None:
        self.warnings.append(f"{path.relative_to(ROOT)}:{line_number}: {message}")


def parse_urf_file(path: Path, state: LintState) -> list[Record]:
    records: list[Record] = []
    current_section = ""

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--") or stripped == "-->":
            continue
        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            current_section = heading_match.group("name")
            continue
        if stripped.startswith("#"):
            continue
        parts = stripped.split("|")
        record_id = parts[0]
        fields: dict[str, str] = {}
        for token in parts[1:]:
            if "=" not in token:
                state.error(path, line_number, f"record token lacks '=': {token!r}")
                continue
            key, value = token.split("=", 1)
            fields[key] = value
        records.append(
            Record(
                file_path=path,
                line_number=line_number,
                section=current_section,
                raw=stripped,
                record_id=record_id,
                fields=fields,
            )
        )
    return records


def parse_stage(record: Record, state: LintState) -> int | None:
    raw_stage = record.fields.get("stage")
    if raw_stage is None:
        state.error(record.file_path, record.line_number, "missing stage field")
        return None
    try:
        stage = int(raw_stage)
    except ValueError:
        state.error(record.file_path, record.line_number, f"invalid stage value {raw_stage!r}")
        return None
    if stage < 0 or stage > 6:
        state.error(record.file_path, record.line_number, f"stage {stage} is outside 0..6")
        return None
    return stage


def parse_pair_id(record: Record, state: LintState) -> tuple[str, str, int] | None:
    match = PAIR_ID_RE.match(record.record_id)
    if not match:
        state.error(record.file_path, record.line_number, f"invalid K/X id {record.record_id!r}")
        return None
    return match.group("prefix"), match.group("kind"), int(match.group("number"))


def resolve_pack_target(family_dir: Path, target: str) -> Path | None:
    target_path = Path(target)
    candidates: list[Path] = []
    if target_path.suffix:
        candidates.append((family_dir / target_path).resolve())
        candidates.append((PACKS_DIR / target_path).resolve())
        candidates.append((ROOT / target_path).resolve())
    else:
        candidates.append((PACKS_DIR / target / "pack.urf.md").resolve())
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def normalize_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def validate_signals(record: Record, state: LintState) -> list[str]:
    signals_value = record.fields.get("signals", "")
    if not signals_value:
        state.error(record.file_path, record.line_number, "routing record is missing signals")
        return []
    signals = signals_value.split(",")
    seen_local: set[str] = set()
    for signal in signals:
        if not signal:
            state.error(record.file_path, record.line_number, "signals contain an empty token")
            continue
        if signal in seen_local:
            state.error(record.file_path, record.line_number, f"signals repeat {signal!r} inside one route")
            continue
        seen_local.add(signal)
        if not LOWER_SIGNAL_RE.match(signal):
            state.error(record.file_path, record.line_number, f"signal {signal!r} must be lowercase literal text")
    return signals


def validate_dense_sequence(index_path: Path, records: list[Record], kind: str, state: LintState) -> None:
    if not records:
        return
    numbers: list[int] = []
    for record in records:
        if not record.record_id.startswith(kind) or not record.record_id[1:].isdigit():
            state.error(record.file_path, record.line_number, f"invalid {kind} id {record.record_id!r}")
            continue
        numbers.append(int(record.record_id[1:]))
    if not numbers:
        return
    if numbers != sorted(numbers):
        state.error(index_path, 1, f"{kind} ids are not ascending")
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        state.error(index_path, 1, f"{kind} ids must be dense with no gaps")


def validate_stage_section(index_path: Path, family_dir: Path, stage_records: list[Record], state: LintState) -> None:
    if family_dir.name != "universal":
        if stage_records:
            state.error(index_path, 1, "## STAGES is only valid in packs/universal/pack.urf.md")
        return

    expected_ids = [f"S{stage:02d}" for stage in range(7)]
    actual_ids = [record.record_id for record in stage_records]
    if actual_ids != expected_ids:
        state.error(index_path, 1, "## STAGES must contain S00 through S06 in order")

    for record in stage_records:
        if not STAGE_ID_RE.match(record.record_id):
            state.error(record.file_path, record.line_number, f"invalid stage id {record.record_id!r}")
        if "name" not in record.fields:
            state.error(record.file_path, record.line_number, "stage record is missing name=")
        if "question" not in record.fields:
            state.error(record.file_path, record.line_number, "stage record is missing question=")


def build_leaf_anchor_text(leaf_path: Path, leaf_records: list[Record], theme: str) -> str:
    chunks = [leaf_path.stem, theme]
    chunks.extend(record.raw for record in leaf_records)
    return normalize_text(" ".join(chunks))


def warn_unanchored_route_signals(
    family_dir: Path,
    route_records: list[Record],
    leaf_registry: dict[str, Record],
    leaf_records_by_name: dict[str, list[Record]],
    state: LintState,
) -> None:
    for route_record in route_records:
        leaf_name = route_record.fields.get("leaf")
        if not leaf_name:
            continue
        registry_record = leaf_registry.get(leaf_name)
        leaf_records = leaf_records_by_name.get(leaf_name)
        if registry_record is None or leaf_records is None:
            continue
        anchor_text = build_leaf_anchor_text(
            family_dir / leaf_name,
            leaf_records,
            registry_record.fields.get("theme", ""),
        )
        for signal in route_record.fields.get("signals", "").split(","):
            if normalize_text(signal) not in anchor_text:
                state.warning(
                    route_record.file_path,
                    route_record.line_number,
                    f"signal {signal!r} has no literal anchor in {leaf_name!r}; consider a more specific selector",
                )


def validate_index(
    family_dir: Path,
    index_path: Path,
    records: list[Record],
    state: LintState,
) -> tuple[set[str], dict[str, Record], list[Record]]:
    stage_records = [record for record in records if record.section == "STAGES"]
    route_records = [record for record in records if record.section == "ROUTING"]
    leaf_records = [record for record in records if record.section == "LEAVES"]

    validate_stage_section(index_path, family_dir, stage_records, state)
    validate_dense_sequence(index_path, route_records, "R", state)
    validate_dense_sequence(index_path, leaf_records, "L", state)

    route_targets: set[str] = set()
    registry_targets: set[str] = set()
    used_signals: dict[str, Record] = {}
    leaf_registry: dict[str, Record] = {}

    for record in route_records:
        if not ROUTING_ID_RE.match(record.record_id) or not record.record_id.startswith("R"):
            state.error(record.file_path, record.line_number, f"invalid routing id {record.record_id!r}")
        has_leaf = "leaf" in record.fields
        has_pack = "pack" in record.fields
        if has_leaf == has_pack:
            state.error(record.file_path, record.line_number, "routing record must contain exactly one of leaf= or pack=")
        for signal in validate_signals(record, state):
            previous = used_signals.get(signal)
            if previous is not None:
                state.error(
                    record.file_path,
                    record.line_number,
                    f"signal {signal!r} already used by {previous.record_id} in {previous.fields.get('leaf', previous.fields.get('pack', 'unknown'))}",
                )
            else:
                used_signals[signal] = record
        if has_leaf:
            leaf_name = record.fields["leaf"]
            target_path = family_dir / leaf_name
            route_targets.add(leaf_name)
            if not target_path.exists():
                state.error(record.file_path, record.line_number, f"leaf target {leaf_name!r} does not exist")
        if has_pack:
            target = record.fields["pack"]
            if resolve_pack_target(family_dir, target) is None:
                state.error(record.file_path, record.line_number, f"pack target {target!r} does not exist")

    for record in leaf_records:
        if not ROUTING_ID_RE.match(record.record_id) or not record.record_id.startswith("L"):
            state.error(record.file_path, record.line_number, f"invalid leaf id {record.record_id!r}")
        leaf_name = record.fields.get("file")
        if not leaf_name:
            state.error(record.file_path, record.line_number, "leaf registry entry is missing file=")
            continue
        registry_targets.add(leaf_name)
        leaf_registry[leaf_name] = record
        if not (family_dir / leaf_name).exists():
            state.error(record.file_path, record.line_number, f"leaf registry target {leaf_name!r} does not exist")
        if "theme" not in record.fields:
            state.error(record.file_path, record.line_number, "leaf registry entry is missing theme=")

    for leaf_name in sorted(route_targets - registry_targets):
        state.error(index_path, 1, f"route target {leaf_name!r} is missing from ## LEAVES")
    for leaf_name in sorted(registry_targets - route_targets):
        state.warning(index_path, 1, f"leaf {leaf_name!r} is registered but not selected by any route")

    actual_leaf_names = {path.name for path in family_dir.glob("*.urf.md") if path.name != "pack.urf.md"}
    for leaf_name in sorted(actual_leaf_names - registry_targets):
        state.warning(index_path, 1, f"leaf file {leaf_name!r} exists on disk but is missing from ## LEAVES")
    return actual_leaf_names, leaf_registry, route_records


def validate_leaf(
    family_dir: Path,
    leaf_path: Path,
    records: list[Record],
    expected_prefix: str,
    state: LintState,
    family_ids: dict[str, Record],
) -> tuple[dict[int, Record], dict[int, Record]]:
    k_records = [record for record in records if record.section == "KERNELS"]
    x_records = [record for record in records if record.section == "EXCLUDES"]

    family_name = family_dir.name
    seen_sections = {record.section for record in records}
    if "KERNELS" not in seen_sections:
        state.error(leaf_path, 1, "leaf file is missing ## KERNELS")
    if "EXCLUDES" not in seen_sections:
        state.error(leaf_path, 1, "leaf file is missing ## EXCLUDES")

    def validate_section(section_records: list[Record], expected_kind: str) -> dict[int, Record]:
        parsed: dict[int, Record] = {}
        order: list[tuple[int, int]] = []
        text_field = "kernel" if expected_kind == "K" else "violation"
        for record in section_records:
            pair_id = parse_pair_id(record, state)
            if pair_id is None:
                continue
            prefix, kind, number = pair_id
            if prefix != expected_prefix:
                state.error(
                    record.file_path,
                    record.line_number,
                    f"id prefix {prefix!r} does not match family {family_name!r} prefix {expected_prefix!r}",
                )
            if kind != expected_kind:
                state.error(record.file_path, record.line_number, f"record is in ## {record.section} but id kind is {kind}")
            if "scope" not in record.fields:
                state.error(record.file_path, record.line_number, f"{record.record_id} is missing required scope= field")
            if text_field not in record.fields:
                state.error(record.file_path, record.line_number, f"{record.record_id} is missing required {text_field}= field")
            stage = parse_stage(record, state)
            if stage is None:
                continue
            if record.record_id in family_ids:
                previous = family_ids[record.record_id]
                state.error(
                    record.file_path,
                    record.line_number,
                    f"id {record.record_id!r} already used in {previous.file_path.relative_to(ROOT)}:{previous.line_number}",
                )
            else:
                family_ids[record.record_id] = record
            if number in parsed:
                previous = parsed[number]
                state.error(
                    record.file_path,
                    record.line_number,
                    f"numeric suffix {number} already used by {previous.record_id!r} in this section",
                )
            else:
                parsed[number] = record
            order.append((stage, number))
        if order != sorted(order):
            state.error(leaf_path, 1, f"records in ## {section_records[0].section if section_records else expected_kind} are not sorted by stage then id")
        return parsed

    return validate_section(k_records, "K"), validate_section(x_records, "X")


def lint_repo() -> int:
    state = LintState()
    family_dirs = sorted(path for path in PACKS_DIR.iterdir() if path.is_dir() and (path / "pack.urf.md").exists())

    validated_leaf_count = 0
    for family_dir in family_dirs:
        index_path = family_dir / "pack.urf.md"
        index_records = parse_urf_file(index_path, state)
        actual_leaf_names, leaf_registry, route_records = validate_index(family_dir, index_path, index_records, state)

        expected_prefix = FAMILY_PREFIXES.get(family_dir.name)
        if expected_prefix is None:
            state.warning(index_path, 1, f"no configured id prefix for family {family_dir.name!r}; skipping K/X prefix checks")
            continue

        family_ids: dict[str, Record] = {}
        family_numbers: dict[str, dict[int, Record]] = {"K": {}, "X": {}}
        leaf_records_by_name: dict[str, list[Record]] = {}

        for leaf_name in sorted(actual_leaf_names):
            leaf_path = family_dir / leaf_name
            leaf_records = parse_urf_file(leaf_path, state)
            leaf_records_by_name[leaf_name] = leaf_records
            validated_leaf_count += 1
            k_records, x_records = validate_leaf(
                family_dir=family_dir,
                leaf_path=leaf_path,
                records=leaf_records,
                expected_prefix=expected_prefix,
                state=state,
                family_ids=family_ids,
            )

            for kind, section_records in (("K", k_records), ("X", x_records)):
                for number, record in section_records.items():
                    previous = family_numbers[kind].get(number)
                    if previous is not None:
                        state.error(
                            record.file_path,
                            record.line_number,
                            f"{kind} suffix {number} already used in {previous.file_path.relative_to(ROOT)}:{previous.line_number}",
                        )
                    else:
                        family_numbers[kind][number] = record

        warn_unanchored_route_signals(
            family_dir=family_dir,
            route_records=route_records,
            leaf_registry=leaf_registry,
            leaf_records_by_name=leaf_records_by_name,
            state=state,
        )

        for kind, other_kind in (("K", "X"), ("X", "K")):
            for number in sorted(set(family_numbers[kind]) - set(family_numbers[other_kind])):
                record = family_numbers[kind][number]
                state.error(record.file_path, record.line_number, f"{kind} suffix {number} has no mirrored {other_kind} entry in family {family_dir.name!r}")

    if state.warnings:
        print("Warnings:")
        for warning in state.warnings:
            print(f"  - {warning}")

    if state.errors:
        print("Errors:")
        for error in state.errors:
            print(f"  - {error}")
        return 1

    print(f"OK: validated {len(family_dirs)} families and {validated_leaf_count} leaf files.")
    if state.warnings:
        print(f"Warnings: {len(state.warnings)}")
    return 0


if __name__ == "__main__":
    sys.exit(lint_repo())
