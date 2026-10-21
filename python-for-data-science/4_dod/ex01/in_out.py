def square(x: int | float) -> int | float:
    """Return x squared."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that repeatedly applies function to x."""
    result = x

    def inner() -> float:
        """Apply function to the previous result and return it."""
        nonlocal result

        result = function(result)
        return result

    return inner
