import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError

    sh, sm, sap, eh, em, eap = match.groups()

    sh = int(sh)
    eh = int(eh)
    sm = int(sm) if sm else 0
    em = int(em) if em else 0

    if sm > 59 or em > 59:
        raise ValueError

    start = to_24(sh, sm, sap)
    end = to_24(eh, em, eap)

    return f"{start} to {end}"


def to_24(h, m, ap):
    if h < 1 or h > 12:
        raise ValueError

    if ap == "AM":
        if h == 12:
            h = 0
    else:  # PM
        if h != 12:
            h += 12

    return f"{h:02}:{m:02}"


if __name__ == "__main__":
    main()
