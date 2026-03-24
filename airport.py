class Airport:
    """Class representing an airport."""

    def __init__(self, name, code, location):
        self.name = name
        self.code = code
        self.location = location

    def get_info(self):
        return f"{self.name} ({self.code}) located in {self.location}."

    def set_location(self, location):
        self.location = location

    def __str__(self):
        return f"Airport({self.name}, {self.code}, {self.location})"
