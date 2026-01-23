# CS50P - Problem Set 2 Logic Pattern Summary Sheet

1. camel.py - Convert camelCase to snake_case
Logic pattern: character scan
· Take input string
· For each character:
  - If uppercase -> print "_" + lowercase
  - Else -> print character
· Build final snake_case output

2. coke.py - Vending Machine Simulation
Logic pattern: loop + subtraction
· Set amount due = 50
· Loop:
  - Take coin input
  - If coin in [25, 10, 5] -> subtract from amount due
  - Print remaining amount
· When amount due <= 0 -> print change owed

3. twttr.py - Remove vowels
Logic pattern: filtering
· Take input string
· For each character:
  - If vowel -> skip
  - Else -> print character
· Output string without vowels

4. plates.py - Vanity Plate Validation
Logic pattern: multi-rule check
· Take plate input
· Check rules in order:
  - Length between 2 and 6
  - First two characters must be letters
  - Once numbers start -> only numbers allowed
  - First number cannot be 0
  - No punctuation or spaces
· If all rules pass -> print "Valid"
· Else -> print "Invalid"

5. nutrition.py - Fruit Calorie Lookup
Logic pattern: dictionary mapping
· Take fruit input
· Normalize to lowercase
· Use dictionary mapping fruit -> calories
· If fruit exists -> print calories
· Else -> no output