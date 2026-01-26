﻿🧩CS50P - Problem Set 1 Logic Pattern Summary Sheet

1. deep_thought.py - Exact Match
Logic pattern: string comparison
· Take user input
· Compare to "42", "forty-two", "forty two"
· If match -> print Yes
· Else -> print No

2. bank.py - Greeting-Based Output
Logic pattern: prefix conditions
· Take user input
· Normalize to lowercase
· If starts with "hello" -> output 0
· Else if starts with "h" -> output 20
· Else -> output 100

3. extensions.py - MIME Type Lookup
Logic pattern: suffix mapping
· Take filename input
· Convert to lowercase
· Extract extension after last dot
· Use dictionary to map extension
· If unknown -> output application/octet-stream

4. interpreter.py - Math Expression Parser
Logic pattern: tokenization + arithmetic
· Take input like "x + y"
· Split into operand1, operator, operand2
· Convert operands to float
· Perform operation
· Print result to one decimal place

5. meal.py - Time-Based Meal Detection
Logic pattern: range check
· Take time input
· Convert to float hour
· If 7.0-8.0 -> breakfast
· If 12.0-13.0 -> lunch
· If 18.0-19.0 -> dinner
