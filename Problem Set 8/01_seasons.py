import datetime
import inflect
import sys

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    minutes = minutes_lived(dob)
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")

def minutes_lived(dob_str):
    try:
        year, month, day = map(int, dob_str.split("-"))
        dob = datetime.date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    today = datetime.date.today()

    if dob > today:
        sys.exit("Invalid date")

    delta = today - dob
    return delta.days * 24 * 60

if __name__ == "__main__":
    main()
