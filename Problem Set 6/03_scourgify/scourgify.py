import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as infile:
            reader = csv.DictReader(infile)
            students = []
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()
