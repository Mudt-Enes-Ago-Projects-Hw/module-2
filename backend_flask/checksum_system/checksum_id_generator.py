"""Checksum-based ID generator utilities.

This module provides helpers that can create identifier segments where the
final digit is a checksum derived from alternating weights and a modulo-7
constraint. It also exposes ``generate_id`` which assembles an 11-digit
identifier made of two checksum-protected segments (4 + 7 digits).
"""

import random

# Predefined *three-digit* numeric codes for supported medicine companies.
# These are the base identifiers for known companies.
# Keys are stored in lowercase for case-insensitive lookup.
COMPANY_CODES = {
    "acme pharma":     "101",
    "healthplus labs": "102",
    "pharmatech":      "103",
    "medicore":        "104",
}

# Reverse lookup table for verifying company segments.
COMPANY_CODE_LOOKUP = {code: name for name, code in COMPANY_CODES.items()}


def _company_code(company_name: str) -> list[int]:
    """
    Convert a company name into its corresponding numeric code digits.

    Args:
        company_name: Human-readable company name (case-insensitive).

    Returns:
        List of integers representing the 3-digit company code.

    Raises:
        ValueError: If company_name is empty or not recognized.
    """
    normalized = (company_name or "").strip().lower()
    if not normalized:
        raise ValueError("company_name must not be empty.")
    try:
        code_str = COMPANY_CODES[normalized]
    except KeyError as exc:
        raise ValueError(f"Unknown company name: {company_name!r}") from exc
    return [int(c) for c in code_str]  # always 3 digits


def _prescribed_digit(prescribed: bool) -> int:
    """Return 1 for prescribed medicine, or 2 for over-the-counter."""
    return 1 if prescribed else 2


class ChecksumIdGenerator:
    """
    Factory class for generating and validating checksum-based identifiers.

    The checksum is computed via a weighted alternating sum:
      - even-indexed digits (0, 2, 4, …) have weight 1
      - odd-indexed digits (1, 3, 5, …) have weight 2
    The result modulo 7 determines the checksum digit required to make the
    total divisible by 7.
    """

    @staticmethod
    def weighted_sum_mod_7(digits: list[int]) -> int:
        """Compute alternating-weighted sum modulo 7."""
        total = 0
        for i, d in enumerate(digits):
            total += d if (i % 2 == 0) else (d * 2)
        return total % 7

    @classmethod
    def compute_checksum(cls, digits: list[int]) -> int:
        """
        Compute a checksum digit (0–6) so that
        (weighted_sum_mod_7(digits + [checksum]) == 0).
        """
        remainder = cls.weighted_sum_mod_7(digits)
        return (-remainder) % 7  # ensures divisibility by 7

    @staticmethod
    def _random_digits(length: int) -> list[int]:
        """Generate a list of random digits (0–9)."""
        return [random.randint(0, 9) for _ in range(length)]

    @classmethod
    def _append_checksum(cls, body_digits: list[int]) -> list[int]:
        """Return a copy of body_digits with the appropriate checksum digit appended."""
        checksum = cls.compute_checksum(body_digits)
        return body_digits + [checksum]

    # ----------------------------------------------------------------------
    #  Segment generation methods
    # ----------------------------------------------------------------------

    @classmethod
    def build_segment_a(cls, company_name: str) -> str:
        """
        Build Segment A (4 digits):
            - first 3 digits: company code
            - last digit: checksum
        """
        code_digits = _company_code(company_name)              # len=3
        seg_a_digits = cls._append_checksum(code_digits)       # len=4
        return "".join(map(str, seg_a_digits))

    @classmethod
    def build_segment_b(cls, prescribed: bool) -> str:
        """
        Build Segment B (7 digits):
            - 1st digit: 1 (prescribed) or 2 (OTC)
            - next 5: random digits
            - final digit: checksum
        """
        payload = [_prescribed_digit(prescribed)] + cls._random_digits(5)  # len=6
        seg_b_digits = cls._append_checksum(payload)                       # len=7
        return "".join(map(str, seg_b_digits))

    @classmethod
    def generate_full_id(cls, *, prescribed: bool, company_name: str, sep: str = "") -> str:
        """
        Return the full 11-digit identifier as:
            SegmentA + [separator] + SegmentB

        Args:
            prescribed: Whether the medicine is prescribed.
            company_name: Company name (must exist in COMPANY_CODES).
            sep: Optional separator (default: "") — e.g., " " for readability.
        """
        a = cls.build_segment_a(company_name)
        b = cls.build_segment_b(prescribed)
        return f"{a}{sep}{b}"


# --------------------------------------------------------------------------
#  Public API wrapper for backwards compatibility
# --------------------------------------------------------------------------

def generate_id(prescribed: bool, company_name: str, *, sep: str = "") -> str:
    """
    Return an 11-digit identifier with two segments and independent checksums.

    Layout:
      - Segment A (4 digits): three-digit company code + checksum digit.
      - Segment B (7 digits): six-digit product payload + checksum digit.
    """
    return ChecksumIdGenerator.generate_full_id(
        prescribed=prescribed, company_name=company_name, sep=sep
    )


# --------------------------------------------------------------------------
#  Identifier validation logic
# --------------------------------------------------------------------------

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
    if company_code not in COMPANY_CODE_LOOKUP:
        return False  # unknown company code

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


# --------------------------------------------------------------------------
#  Self-test / demonstration when run directly
# --------------------------------------------------------------------------
if __name__ == "__main__":
    gen = ChecksumIdGenerator()

    # --- basic tests ---
    sample = [1, 2, 3, 4]  # contributes 1 + 4 + 3 + 8 = 16; 16 % 7 = 2
    print("weighted_sum_mod_7(sample):", gen.weighted_sum_mod_7(sample))  # -> 2
    print("compute_checksum(sample):", gen.compute_checksum(sample))      # -> 5

    # --- segment generation ---
    print("Segment A (Medicore):", gen.build_segment_a("Medicore"))       # Example: '104x'
    print("Segment B (prescribed):", gen.build_segment_b(True))           # Example: '1xxxxxC'

    # --- full ID and verification ---
    sample_id = generate_id(True, "Acme Pharma")
    print("Full ID (no space):", sample_id, "valid?", verify_id(sample_id))

    spaced_id = ChecksumIdGenerator.generate_full_id(
        prescribed=False,
        company_name="Pharmatech",
        sep=" ",
    )
    print("Full ID (spaced):", spaced_id, "valid?", verify_id(spaced_id))

    # --- demonstrate failure cases ---
    """10151137443 is generated by generate id"""
    print("Tampered ID:", "10151137443", "valid?", verify_id("10151137443"))
    print("Tampered ID:", "10151137442", "valid?", verify_id("10151137442"))
    print("Tampered ID:", "10121137443", "valid?", verify_id("10121137443"))