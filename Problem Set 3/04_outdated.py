months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        # Numeric format: MM/DD/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        # Written format: Month DD, YYYY
        else:
            if "," not in date:
                raise ValueError

            month_name, rest = date.split(" ", 1)
            day, year = rest.split(", ")
            day = int(day)
            year = int(year)

            if month_name in months and 1 <= day <= 31:
                month = months.index(month_name) + 1
                break

    except ValueError:
        pass

print(f"{year:04d}-{month:02d}-{day:02d}")
