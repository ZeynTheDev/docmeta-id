import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


PROJECT_ROOT = Path(__file__).resolve().parents[1]

MANIFEST_PATH = PROJECT_ROOT / "pilot" / "metadata.jsonl"
IMAGE_ROOT = MANIFEST_PATH.parent
SCHEMA_PATH = PROJECT_ROOT / "schemas" / "document_record.schema.json"


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    seen_ids: set[str] = set()
    errors: list[str] = []

    with MANIFEST_PATH.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(
                    f"Line {line_number}: Invalid JSON: {exc}"
                )
                continue

            for error in validator.iter_errors(record):
                errors.append(
                    f"Line {line_number}: {error.message}"
                )

            document_id = record.get("document_id")

            if document_id in seen_ids:
                errors.append(
                    f"Line {line_number}: Duplicate ID: {document_id}"
                )
            seen_ids.add(document_id)

            file_name = record.get("file_name")

            if file_name:
                image_path = (
                    IMAGE_ROOT / file_name
                ).resolve()

                try:
                    image_path.relative_to(IMAGE_ROOT.resolve())
                except ValueError:
                    errors.append(
                        f"Line {line_number}: Image path escapes dataset root"
                    )
                    continue

                if not image_path.is_file():
                    errors.append(
                        f"Line {line_number}: Image not found: {file_name}"
                    )

    if errors:
        print("Validation FAILED:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"Validation PASSED: {len(seen_ids)} documents")


if __name__ == "__main__":
    main()

