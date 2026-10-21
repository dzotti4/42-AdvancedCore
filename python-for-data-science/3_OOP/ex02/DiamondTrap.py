from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Respresent Joffrey as a Baratheon and Lannister king."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a king."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Return the king's eyes color."""
        return self.eyes

    def set_eyes(self, color):
        """Set the king's eyes color."""
        self.eyes = color

    def get_hairs(self):
        """Return the king's hairs color."""
        return self.hairs

    def set_hairs(self, color):
        """Set king's hairs color."""
        self.hairs = color
