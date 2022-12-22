class NameGenerator:
    def __init__(self):
        """Prints the welcome"""
        print("Welcome to the Band Name Generator")

    def generate_name(self):
        """Asks for the city and pet name and generates a aband name from it."""
        city = input("What city did you grow up in?\n  ")
        pet = input("What was the name of your first pet?  \n  ")
        band_name = city + pet
        print(f"You new band name is: {band_name}")
