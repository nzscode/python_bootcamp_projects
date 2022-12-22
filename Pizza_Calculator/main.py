# Pizza Calculator
from pizzacalculator import pizza_calculator
calculator = pizza_calculator()
pizza_size = calculator.pizza_order()
pizza_price = calculator.pizza_price(pizza_size)
pepperoni = calculator.add_pepperoni(pizza_size)
cheese = calculator.add_cheese()
total = float(pizza_price) + float(pepperoni) + float(cheese)
print(f"Your final bill is ${total:.2f}")
