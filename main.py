"""Iron and Regret — a one-line museum placard for an ordinary office
object, written as if it were an ancient artifact.

The Placard gate: /output/entry.txt must hold exactly one line of
UTF-8 text, 1-180 characters, not whitespace-only. The placard names
a stapler, gives it a catalogue date (c. 1994), a material (iron),
and a donor (the Accounts Department), then lands the dry joke on
the last clause: it bound the last budget nobody read.
"""

import os

LINE = (
    "Stapler, c. 1994. Iron and regret. Donated by the Accounts "
    "Department after binding the last budget nobody read."
)


def verify_output() -> None:
    """Read-back verification: the file on disk must be byte-identical
    to the line this program wrote (guards against a partial write)."""
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == LINE.encode("utf-8"), (
        f"read-back mismatch: {len(on_disk)} bytes on disk, "
        f"{len(LINE.encode('utf-8'))} expected"
    )


def main() -> None:
    # Gate assertions: one line, 1-180 chars, not whitespace-only.
    assert LINE.strip(), "line must not be whitespace-only"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, gate is 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
