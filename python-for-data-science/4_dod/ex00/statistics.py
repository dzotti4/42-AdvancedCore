from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print requested statistics from given numbers."""
    for value in kwargs.values():
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            print(f"mean : {get_mean(args)}")
        elif value == "median":
            print(f"median : {get_median(args)}")
        elif value == "quartile":
            print(f"quartile : {get_quartile(args)}")
        elif value == "std":
            print(f"std : {get_std(args)}")
        elif value == "var":
            print(f"var : {get_var(args)}")


def get_mean(numbers: tuple) -> float:
    """Return the mean of the given numbers."""
    total = 0

    for number in numbers:
        total = total + number
    return total / len(numbers)


def get_median(numbers: tuple) -> float:
    """Return the median of the given numbers."""
    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle]
    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2


def get_quartile(numbers: tuple) -> list:
    """Return the quartile of the given numbers."""
    sorted_numbers = sorted(numbers)
    first_index = int(len(sorted_numbers) * 0.25)
    second_index = int(len(sorted_numbers) * 0.75)

    return [
        float(sorted_numbers[first_index]),
        float(sorted_numbers[second_index]),
    ]


def get_var(numbers: tuple) -> float:
    """Return the variance of the given numbers."""
    mean = get_mean(numbers)
    total = 0

    for number in numbers:
        total = total + ((number - mean) ** 2)
    return total / len(numbers)


def get_std(numbers: tuple) -> float:
    """Return the standard deviation of the given numbers."""
    return get_var(numbers) ** 0.5
