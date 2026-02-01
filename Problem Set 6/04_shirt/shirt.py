import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_exts = [".jpg", ".jpeg", ".png"]

    if not any(input_file.lower().endswith(ext) for ext in valid_exts):
        sys.exit("Invalid input")

    if not any(output_file.lower().endswith(ext) for ext in valid_exts):
        sys.exit("Invalid output")

    if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    resized = ImageOps.fit(input_image, shirt.size)
    resized.paste(shirt, shirt)
    resized.save(output_file)

if __name__ == "__main__":
    main()
