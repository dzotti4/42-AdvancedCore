from typing import Any


def callLimit(limit: int):
    """Return a decorator that allows a function to be called limit times."""
    count = 0

    def callLimiter(function):
        """Wrap function so it stops running after the call limit."""

        def limit_function(*args: Any, **kwds: Any):
            """Call function if the limit is not reached, else print error."""
            nonlocal count

            if count < limit:
                count = count + 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
