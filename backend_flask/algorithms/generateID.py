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

class Preset:

    COMPANY_CODES = {
        "acme pharma":     "101",
        "healthplus labs": "102",
        "pharmatech":      "103",
        "medicore":        "104",
    }

    # Reverse lookup table for verifying company segments.
    COMPANY_CODE_LOOKUP = {code: name for name, code in COMPANY_CODES.items()}

    @classmethod
    def _company_code(cls, company_name: str = None, company_code: str = None) -> list[int]:
        """
        Convert a company name or code into its corresponding numeric code digits.

        Args:
            company_name: Human-readable company name (case-insensitive).
            company_code: Direct 3-digit company code (e.g., "101", "102").

        Returns:
            List of integers representing the 3-digit company code.

        Raises:
            ValueError: If both or neither parameters are provided, or if invalid.
        """
        if company_code is not None:
            # Direct company code provided
            code_str = str(company_code).strip()
            if len(code_str) != 3 or not code_str.isdigit():
                raise ValueError(f"company_code must be exactly 3 digits, got: {company_code!r}")
            return [int(c) for c in code_str]
        
        if company_name is not None:
            # Legacy: lookup by company name
            normalized = company_name.strip().lower()
            if not normalized:
                raise ValueError("company_name must not be empty.")
            try:
                code_str = cls.COMPANY_CODES[normalized]
            except KeyError as exc:
                raise ValueError(f"Unknown company name: {company_name!r}") from exc
            return [int(c) for c in code_str]  # always 3 digits
        
        raise ValueError("Either company_name or company_code must be provided.")

    @staticmethod
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
    def build_segment_a(cls, company_name: str = None, company_code: str = None) -> str:
        """
        Build Segment A (4 digits):
            - first 3 digits: company code
            - last digit: checksum
        
        Args:
            company_name: Company name (legacy, looked up in COMPANY_CODES).
            company_code: Direct 3-digit company code (e.g., "101").
        """
        code_digits = Preset._company_code(company_name=company_name, company_code=company_code)  # len=3
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
        payload = [Preset._prescribed_digit(prescribed)] + cls._random_digits(5)  # len=6
        seg_b_digits = cls._append_checksum(payload)                       # len=7
        return "".join(map(str, seg_b_digits))

    @classmethod
    def generate_full_id(cls, *, prescribed: bool, company_name: str = None, company_code: str = None, sep: str = "") -> str:
        """
        Return the full 11-digit identifier as:
            SegmentA + [separator] + SegmentB

        Args:
            prescribed: Whether the medicine is prescribed.
            company_name: Company name (must exist in COMPANY_CODES, legacy).
            company_code: Direct 3-digit company code (e.g., "101").
            sep: Optional separator (default: "") — e.g., " " for readability.
        """
        a = cls.build_segment_a(company_name=company_name, company_code=company_code)
        b = cls.build_segment_b(prescribed)
        return f"{a}{sep}{b}"


# --------------------------------------------------------------------------
#  Public API wrapper for backwards compatibility
# --------------------------------------------------------------------------

def generate_id(prescribed: bool, company_name: str = None, company_code: str = None, *, sep: str = "") -> str:
    """
    Return an 11-digit identifier with two segments and independent checksums.

    Layout:
      - Segment A (4 digits): three-digit company code + checksum digit.
      - Segment B (7 digits): six-digit product payload + checksum digit.
    
    Args:
        prescribed: Whether the medicine is prescribed.
        company_name: Company name (legacy, looked up in COMPANY_CODES).
        company_code: Direct 3-digit company code (e.g., "101", "102").
        sep: Optional separator between segments (default: "").
    """
    return ChecksumIdGenerator.generate_full_id(
        prescribed=prescribed, company_name=company_name, company_code=company_code, sep=sep
    )
