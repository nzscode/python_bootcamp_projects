class Tip_Calculate:
    def __init__(self):
        """prints out a greeting."""
        print("Welcome to the Tip Calculator")

    def calculate(self):
        """Given the bill total, tip percent and number of payers, calculates how much each payer must pay."""
        bill_total = float(input("What is your total bill?  \n"))
        tip_percentage = input("What is the tip percentage? Choose 10%, 12% or 15% \n")
        final_percent = float("1." + tip_percentage)
        payers = int(input("How many will be splitting the bill?  \n"))

        per_payer = (bill_total / payers) * final_percent

        print(f"Each person should pay: ${per_payer:.2f}")
