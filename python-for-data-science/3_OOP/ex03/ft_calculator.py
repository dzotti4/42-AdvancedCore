class calculator:
    """Represent a calculator for vector and scalar operations."""

    def __init__(self, vector):
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each value of the vector."""
        result = []
        for value in self.vector:
            result.append(value + object)
        self.vector = result
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each value of the vector by a scalar."""
        result = []
        for value in self.vector:
            result.append(value * object)
        self.vector = result
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each value of the vector."""
        result = []
        for value in self.vector:
            result.append(value - object)
        self.vector = result
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each value if the vector by a scalar."""
        if object == 0:
            print("Error: division by zero.")
            return
        result = []
        for value in self.vector:
            result.append(value / object)
        self.vector = result
        print(self.vector)
