"""Simple manual checks for the checksum ID generator.

Run with ``python3 projects_semster1/checksum_system/test_checksum_id_generator.py``.
This script shows how to call ``generate_id`` and validates that the results
follow the expected structure.
"""

import os
import random
import sys

# --------------------------------------------------------------------------
#  Configure import path so that this script can find the main project module.
# --------------------------------------------------------------------------

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))       # Folder where this script resides.
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))   # Go up two levels to project root.

# Add project root to sys.path to allow relative imports to work
# even when running this test script directly.
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Import functions under test from your main generator module.
from projects_semster1.checksum_system.checksum_id_generator import generate_id, verify_id


def show_sample_ids():
    """
    Generate and display sample IDs for multiple companies and prescription types.
    Each generated ID is validated immediately to confirm correctness.
    """

    random.seed(42)  # Fixed seed for reproducible test output.

    # Define test cases: (is_prescribed, company_name)
    cases = [
        (True, "Acme Pharma"),
        (False, "Pharmatech"),
        (True, "Medicore"),
        (False, "HealthPlus Labs"),
    ]

    # ----------------------------------------------------------------------
    # Generate an ID for each case, verify it, and print results.
    # ----------------------------------------------------------------------
    for prescribed, company_name in cases:
        identifier = generate_id(prescribed, company_name)   # Create full ID.
        is_valid = verify_id(identifier)                     # Verify checksum and structure.
        print(
            f"prescribed={prescribed:<5} company={company_name:<18} "
            f"id={identifier} valid={is_valid}"
        )

    # ----------------------------------------------------------------------
    # Demonstrate checksum validation: introduce a controlled typo.
    # ----------------------------------------------------------------------
    example = generate_id(True, "Acme Pharma")
    # Modify the last digit (checksum) to a different one.
    typo = example[:-1] + str((int(example[-1]) + 1) % 10)

    print(f"\nOriginal ID : {example} -> verify_id={verify_id(example)}")
    print(f"Typo version: {typo} -> verify_id={verify_id(typo)}")
    # Expected: original -> True, typo -> False


if __name__ == "__main__":
    # Entry point when script is run directly from the command line.
    # Runs the manual test and prints formatted sample results.
    show_sample_ids()