"""Identifier verification helpers."""

try:
    from .generateID import ChecksumIdGenerator, Preset
except ImportError:  # Allow direct script execution within the algorithms folder.
    from generateID import ChecksumIdGenerator, Preset  # type: ignore

__all__ = ["verify_id"]


def verify_id(identifier: str) -> bool:
    """
    Validate an identifier string for correct length, content, and checksum.

    Returns True if:
      - Identifier contains only digits and spaces.
      - Length (digits only) == 11.
      - Company and product segments have valid checksums and codes.

    Otherwise returns False.
    """
    if not identifier:
        return False

    stripped = identifier.strip()
    if not stripped:
        return False

    # Only allow digits and spaces (so "1234 5678901" is valid format)
    for ch in stripped:
        if not (ch.isdigit() or ch.isspace()):
            return False

    digits_only = "".join(ch for ch in stripped if ch.isdigit())
    if len(digits_only) != 11:
        return False

    # Split into segments.
    segment_a = digits_only[:4]
    segment_b = digits_only[4:]

    # --- Validate company segment ---
    company_code = segment_a[:3]
    # Accept any 3-digit company code (now that codes are dynamic in database)
    if not company_code.isdigit():
        return False  # company code must be digits
    
    company_digits = [int(c) for c in segment_a[:-1]]
    company_checksum = int(segment_a[-1])
    if ChecksumIdGenerator.compute_checksum(company_digits) != company_checksum:
        return False  # company checksum invalid

    # --- Validate product segment ---
    if len(segment_b) != 7:
        return False

    type_digit = int(segment_b[0])
    if type_digit not in (1, 2):
        return False  # must be 1 (prescribed) or 2 (OTC)

    product_digits = [int(c) for c in segment_b[:-1]]
    product_checksum = int(segment_b[-1])
    if ChecksumIdGenerator.compute_checksum(product_digits) != product_checksum:
        return False  # product checksum invalid

    return True
