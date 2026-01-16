def camel_to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

def main():
    camel = input("camelCase: ")
    print("snake_case:", camel_to_snake(camel))

if __name__ == "__main__":
    main()
