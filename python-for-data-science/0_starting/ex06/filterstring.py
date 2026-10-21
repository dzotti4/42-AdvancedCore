import sys


def main():
    """Run the filterstring progam."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    text = sys.argv[1]

    try:
        number = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = text.split()

    result = [
        word for word in words
        if (lambda current: len(current) > number)(word)
    ]

    print(result)


if __name__ == "__main__":
    main()
