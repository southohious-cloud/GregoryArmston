def main():
    groceries = {}

    while True:
        try:
            item = input().strip().upper()
            if item:
                groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            break

    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")


main()
