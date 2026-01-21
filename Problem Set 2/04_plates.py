"""
validation logic for vanity plates
"""

def is_valid(plate: str) -> bool:
    # Rule 1: Length must be between 2 and 6 characters
    if not (2 <= len(plate) <= 6):
        return False

    # Rule 2: First two characters must be letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    number_started = False

    for char in plate:
        # Rule 3: Numbers only at the end, and first number cannot be zero
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        else:
            # If letters appear after numbers, invalid
            if number_started:
                return False

        # Rule 4: Only alphanumeric characters allowed
        if not char.isalnum():
            return False

    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
