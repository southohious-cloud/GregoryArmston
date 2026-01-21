def main():
    fraction = get_fraction()
    percent = round(fraction * 100)

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            if x < 0 or y < 0:
                raise ValueError

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError

            return x / y

        except ValueError:
            continue
        except ZeroDivisionError:
            continue



main()
