import sys

def count_lines(file):
    count = 0
    for line in file:
        stripped = line.strip()
        if stripped == "":
            continue
        if stripped.startswith("#"):
            continue
        count += 1
    return count

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            count = count_lines(file)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)

if __name__ == "__main__":
    main()
