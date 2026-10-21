class calculator:
    """Represent a calculator for vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = 0
        index = 0
        while index < len(V1):
            result += V1[index] * V2[index]
            index += 1
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors and print the result."""
        result = []
        index = 0
        while index < len(V1):
            result.append(float(V1[index] + V2[index]))
            index += 1
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors and print the result."""
        result = []
        index = 0
        while index < len(V1):
            result.append(float(V1[index] - V2[index]))
            index += 1
        print(f"Sous Vector is: {result}")
