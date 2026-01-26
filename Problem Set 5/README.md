🧩 Problem Set 5 — Unit Tests

Overview  
Problem Set 5 expands on writing predictable, testable Python functions by introducing automated validation with pytest.  
Each test file targets a specific program and ensures correct logic, edge‑case handling, and consistent behavior.

Files  
1. test_twttr.py  
   Validates the shorten() function by checking vowel removal, mixed‑case handling, and behavior with both vowel‑only and vowel‑free strings.

2. test_bank.py  
   Confirms correct return values for greetings, including “hello” variations, words beginning with h, and all other inputs.

3. test_plates.py  
   Tests vanity plate validation rules, including length limits, starting letters, number placement, leading zero restrictions, and alphanumeric requirements.

4. test_fuel.py  
   Ensures convert() and gauge() behave predictably by testing valid fractions, zero‑division errors, X > Y errors, and gauge output for E, F, and percentage ranges.