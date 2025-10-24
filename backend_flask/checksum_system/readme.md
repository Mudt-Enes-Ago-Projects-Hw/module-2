# 🧮 Checksum-based ID Generator

**Tiny, dependency-free utilities for creating and validating 11-digit identifiers with an embedded mod-7 checksum.**  
Each identifier is composed of two independently protected segments:  
`4 digits (company)` + `7 digits (product/prescription payload)`

**Language:** Python 3.10+ (uses `list[int]` annotations)  
**Location:** `projects_semster1/checksum_system/`

---

## ✨ What it does

- Generate an ID for a known company and prescription type.  
- Validate an ID’s structure and checksums.  
- Enforce a fixed set of 3-digit company codes.

> No external libraries required.

---

## 🧱 ID layout

<br/>AAAAAAAAAAA  (11 digits total)<br/>
<br/>││││││││││└─ Segment B checksum (mod 7)<br/>
<br/>│││││││││└── 5 random digits (0-9)<br/>
<br/>││││││││└─── Type digit: 1=prescribed, 2=OTC<br/>
<br/>││││└──────── Segment A checksum (mod 7)<br/>
<br/>│││└───────── 3-digit company code (ASCII digits only)<br/>
<br/>└──────────── Segment A (4) + Segment B (7)<br/>

You may optionally insert a separator (e.g., a space) between segments when formatting for display.  
Validation accepts digits with optional whitespace (including tabs/newlines), but the digits-only length must be **11**.

---

## 🔢 Checksum algorithm (brief)

- Traverse digits left to right.  
- Even indices (0-based): weight **1**; odd indices: weight **2**.  
- Sum the weighted digits and take **mod 7**.  
- The checksum digit is chosen so that `total % 7 == 0`.  

That is:  

checksum = (-weighted_sum) % 7   → checksum ∈ {0..6}

Both segments have independent checksums using this same rule.

---

## 🗂️ Company codes

**Built-in mapping (lower-cased keys):**

| Company name      | Code |
|--------------------|------|
| acme pharma        | 101  |
| healthplus labs    | 102  |
| pharmatech         | 103  |
| medicore           | 104  |

To add a company, extend `COMPANY_CODES` in `checksum_id_generator.py`, keeping three integer digits as the value.

---

## 📦 Public API

```python
from projects_semster1.checksum_system.checksum_id_generator import (
    generate_id, verify_id, ChecksumIdGenerator
)

# Generate a full ID (11 digits; optional separator for readability)
identifier = generate_id(prescribed=True, company_name="Acme Pharma")            # e.g., '1011xxxxxC'

identifier_spaced = ChecksumIdGenerator.generate_full_id(
    prescribed=False, company_name="Pharmatech", sep=" "
)                                                                               # e.g., '103C 2xxxxxC'

# Validate an ID (tolerates whitespace between/within segments)
is_valid = verify_id(identifier)        # -> True/False
is_also_valid = verify_id(identifier_spaced)  # -> True

# Segment builders (if you need them)
a = ChecksumIdGenerator.build_segment_a("Medicore")         # '104C' (4 digits)
b = ChecksumIdGenerator.build_segment_b(prescribed=True)    # '1xxxxxC' (7 digits)

Note: C above denotes a checksum digit 0–6, not a literal “C”.

```
## ▶️ Running the demo/test script

A simple manual test script is provided:

projects_semster1/checksum_system/test_checksum_id_generator.py

Run:

python3 projects_semster1/checksum_system/test_checksum_id_generator.py

What it shows
	•	Generates sample IDs for multiple companies and both prescription types.
	•	Verifies each ID and prints valid=True.
	•	Demonstrates that a single-digit typo causes verify_id(...) to fail.

The script seeds the RNG for reproducible output.

---

📏 Validation rules (verify_id() checks)
	1.	Input is non-empty; digits and whitespace only are allowed.
	2.	Total digit count equals 11 (whitespace ignored).
	3.	Segment A
	•	First 3 digits form a known company code.
	•	4th digit matches the computed checksum.
	4.	Segment B
	•	First digit is 1 (prescribed) or 2 (OTC).
	•	7th digit matches the computed checksum.

✅ Returns True only if all conditions are satisfied.

---

🧪 Reproducible example (pseudo-output)

prescribed=True  company=Acme Pharma       id=1011xxxxxC  valid=True
prescribed=False company=Pharmatech        id=1032xxxxxC  valid=True
...

Original ID : 1011xxxxxC -> verify_id=True
Typo version: 1011xxxxxD -> verify_id=False

(Where x are random digits and C/D are checksum digits in 0..6.)

---

⚠️ Notes & gotchas
	•	The weighting starts at the leftmost digit (index 0).
If you adapt this for other systems, note some weight from the right.
	•	verify_id() currently accepts any Unicode digits/whitespace via str.isdigit() / str.isspace().
If you require ASCII-only input, normalize or tighten the checks.
	•	The random payload may contain zeros (by design). This is fine for uniqueness and entropy.

---

🙋 FAQ

Q: Why 11 digits?
A: Compact format with two independent checksums: 4 (company+checksum) + 7 (payload+checksum).

Q: Can I print with a space?
A: Yes. Use sep=" " in generate_full_id. Validation ignores whitespace.

Q: How do I add a new company?
A: Extend COMPANY_CODES with a lower-cased name and a three-digit string code
(e.g., "newco": "105").

---
