def main():
    # Prompt the user for input
    msg = input()
    # Convert emoticons to emojis
    converted_msg = convert(msg)
    # Print the result
    print(converted_msg)

def convert(text):
    # Replace :) with 🙂
    text = text.replace(":)", "🙂")
    # Replace :( with 🙁
    text = text.replace(":(", "🙁")
    # Return the changed text
    return text

# Call main at the bottom
main()
