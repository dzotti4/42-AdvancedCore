import sys
import string


def main():
    """Run the program."""
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        text += "\n"
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    upper = 0
    lower = 0
    digit = 0
    spaces = 0
    punctuation = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            spaces += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    main()
