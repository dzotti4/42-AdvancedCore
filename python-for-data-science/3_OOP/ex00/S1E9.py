from abc import ABC, abstractmethod


class Character(ABC):
    """Represent an abstract Game of Thrones character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a name and life state."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character life state to dead."""
        self.is_alive = False


class Stark(Character):
    """Respresent a Stark character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)
