def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate BMI values from height and weight list."""
    if not isinstance(height, list):
        raise AssertionError("height must be a list")
    if not isinstance(weight, list):
        raise AssertionError("weight must be a list")
    if len(height) != len(weight):
        raise AssertionError("height and weight must have the same size")

    result = []
    i = 0
    while i < len(height):
        if not isinstance(height[i], (int, float)):
            raise AssertionError("height values must be int or float")
        if not isinstance(weight[i], (int, float)):
            raise AssertionError("weight values must be int or float")
        if height[i] == 0:
            raise AssertionError("height values cannot be zero")
        bmi = weight[i] / (height[i] * height[i])
        result.append(bmi)
        i += 1
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for every BMI value above the limit."""
    if not isinstance(bmi, list):
        raise AssertionError("bmi must be a list")
    if not isinstance(limit, int):
        raise AssertionError("limit must be an int")

    result = []
    i = 0
    while i < len(bmi):
        if not isinstance(bmi[i], (int, float)):
            raise AssertionError("bmi values must be int or float")
        if bmi[i] > limit:
            result.append(True)
        else:
            result.append(False)
        i += 1
    return result


def main():
    """Run basic tests."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
