class pizza_calculator:
    def __init__(self):
        print("Welcome to the pizza calculator.")


    def pizza_order(self):
        """Return size"""
        size_choice = input("What size pizza are you ordering? 's', 'm', or 'l'.").lower()
        return size_choice

    def pizza_price(self, size):
        """Returns price of chosen size"""
        size_price = [
            {
                "size": "s",
                "price": 15,
            },
            {
                "size": "m",
                "price": 20,
            },
            {
                "size": "l",
                "price": 25
            }
        ]
        for i in range(len(size_price)):
            if size in size_price[i]["size"]:
                return int(size_price[i]["price"])

    def add_pepperoni(self, size):
        """Returns extra cost of pepperoni"""
        pepperoni = input("Would you like pepperoni? Type 'y' or 'n'.")
        if size == 's' and pepperoni == 'y':
            return 2
        else:
            if pepperoni == 'y':
                return 3

    def add_cheese(self):
        """Returns extra cost of cheese"""
        cheese = input("Would you like extra cheese? Type 'y' or 'n'.")
        if cheese == 'y':
            return 1
        else:
            return 0


