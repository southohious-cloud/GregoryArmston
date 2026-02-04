import re


def main():
    print(parse(input("URL: ")))


def parse(s):
    # Pattern for standard watch URLs
    watch_pattern = r"^https?://(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)$"

    # Pattern for iframe embed URLs
    embed_pattern = r'^<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"></iframe>$'

    # Try watch pattern
    if match := re.search(watch_pattern, s):
        return f"https://youtu.be/{match.group(1)}"

    # Try embed pattern
    if match := re.search(embed_pattern, s):
        return f"https://youtu.be/{match.group(1)}"

    return None


if __name__ == "__main__":
    main()
