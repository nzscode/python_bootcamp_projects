#FileNotFound
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError(f"The height entered is not possible.")
elif weight > 100:
    raise ValueError(f"The weight entered is not possible.")
else:
    bmi = weight / height ** 2
    print(f"This is your BMI {bmi}")
