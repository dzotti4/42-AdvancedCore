def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D list and print old and new shapes."""
    if not isinstance(family, list):
        raise AssertionError("family must be a list")
    if len(family) == 0:
        raise AssertionError("family cannot be empty")
    if not isinstance(start, int):
        raise AssertionError("start must be an int")
    if not isinstance(end, int):
        raise AssertionError("end must be an int")

    row_size = len(family[0])
    i = 0
    while i < len(family):
        if not isinstance(family[i], list):
            raise AssertionError("family rows must be lists")
        if len(family[i]) != row_size:
            raise AssertionError("family rows must have the same size")
        i += 1

    old_shape = (len(family), len(family[0]))
    print(f"My shape is : {old_shape}")

    new_family = family[start:end]

    new_shape = (len(new_family), len(new_family[0]))
    print(f"My new shape is : {new_shape}")

    return new_family


def main():
    """Run basic tests."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
