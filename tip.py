def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # # Remove the leading '$' sign
    d_without_dollar = d.replace("$", "")
    # Convert the remaining string to a float and return it
    return float(d_without_dollar)


def percent_to_float(p):
    # Remove the trailing '%' sign
    p_without_percent = p.replace("%", "")
    # Convert to float and divide by 100 to get the decimal representation
    return float(p_without_percent) / 100


main()
