from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the Baratheon physical description."""
        return "Vector: ('Baratheon', 'brown', 'dark')"

    def __repr__(self):
        """Return the Baratheon official representation."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return the Lannister physical description."""
        return "Vector: ('Lannister', 'blue', 'light')"

    def __repr__(self):
        """Return the Lannister official representation."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character."""
        return cls(first_name, is_alive)
