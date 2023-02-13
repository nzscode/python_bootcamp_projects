def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(1, 2, 3))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.windows = kw.get("windows")
        self.wheels = kw.get("wheels")
        self.car_type()
        self.wheel_multiply()

    def wheel_multiply(self):
        if self.wheels:
            print(self.wheels * 10)

    def car_type(self):
        if self.make == "Toyota":
            print("Toyota: Camri")


car = Car(make="Toyota", wheels=3)
print(f"Windows = {car.windows}")
