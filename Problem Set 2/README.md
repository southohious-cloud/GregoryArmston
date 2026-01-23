# CS50P - Problem Set 2 Logic Pattern Summary Sheet

1. camel.py - camelCase -> snake_case
Logic Pattern: Character-by-character transformation
· Loop through each character
· If the character is uppercase:
  · Add an underscore
  · Convert it to lowercase
· Otherwise, append as-is
· Build the output string sequentially

2. coke.py - Coke Machine Simulation
Logic Pattern: Input validation + running total
· Start with 50 cents owed
· Loop until the total reaches 0
· Accept only 5, 10 or 25
· Subtract valid coins from the total
· Ignore invalid coins
· When total <= 0, output change owed

3. twttr.py - Remove Vowels
Logic Pattern: Filter pattern
· Define a set of vowels
· Loop through each character
· Skip vowels
· Append all other characters
· Preserve original order

4. plates.py - Vanity Plate Validation
Logic Pattern: Multi-rule validation with early returns
Rules enforced in order:
· (1) Length must be 2-6 characters
· (2) First two characters must be letters
· (3) Numbers may appear only at the end
· (4) First number cannot be zero
· (5) Only alphanumeric characters allowed
Each rule can fail immediately.

5. nutrition.py - Fruit -> Calories Lookup
Logic Pattern: Dictionary lookup
· Normalize input to lowercase
· Use a dictionary mapping fruit -> calories
· If the fruit exists, print its calories
· If not, print nothing