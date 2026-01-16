# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Split the expression into x (first int), y (operator), and z (second int)
x, y, z = expression.split(" ")

# Convert x and z to floats to prepare for calculation
n1 = float(x)
n2 = float(z)

# Calculate based on the operator y
if y == "+":
    result = n1 + n2
elif y == "-":
    result = n1 - n2
elif y == "*":
    result = n1 * n2
elif y == "/":
    # z is assumed not to be 0 per instructions
    result = n1 / n2

# Output the result formatted to one decimal place
print(f"{result:.1f}")


