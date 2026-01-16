"""
twttr.py — Utility and main program for removing vowels from text.
"""

VOWELS = "aeiouAEIOU"

def shorten(text: str) -> str:
    """
    Return the text with all vowels removed.
    """
    result = ""
    for char in text:
        if char not in VOWELS:
            result += char
    return result

def main():
    text = input("Input: ")
    print("Output:", shorten(text))

if __name__ == "__main__":
    main()
