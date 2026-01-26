from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # If no arguments, choose random font
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    # If arguments, must be: -f FONTNAME
    elif len(sys.argv) == 3 and sys.argv[1] == "-f" and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
