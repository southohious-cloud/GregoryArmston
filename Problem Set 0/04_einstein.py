def main():
    # Prompt the user for mass in kilograms
    mass = int(input("m: "))

    # Define the speed of light (meters per second)
    c = 300000000

    # Calculate energy using E = mc^2
    energy = mass * (c ** 2)

    # Output the result as an integer
    print(f"E: {energy}")

main()
