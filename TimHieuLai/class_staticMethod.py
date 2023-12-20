class Car():
    tax = 1
    car_number = 0
    def __init__(self, brand, model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        Car.car_number += 1

    # Regular method có thể được gọi bởi các instance nhưng không được gọi bằng class
    def GetValue(self):
        return (self.price * self.tax)
    
    def set_tax_regular():
        Car.tax = 1.5
    
    @classmethod
    def set_tax (cls):
        cls.tax = 1.5

    # class method có thể được gọi bởi các instance và class và gọi được init
    # đầu vào phải có giá trị khởi tạo đầu tiên
    @classmethod
    def from_string(cls, car_string):
        brand, model, founded_year, price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand, model, founded_year, price)
    
    # static method có thể được gọi bởi các instance và class và không gọi được init
    @staticmethod
    def check_price(price):
        if price <= 1000:
            return "This car is cheap!"
        else:
            return "This car is expensive!"

car_temp = "Toyoto-Camry-1969-800"
car_1=Car("Vinfast", "LuxA", 2017, 1500)
car_2=Car("BMW", "i320", 1916, 700)
car_3= Car.from_string(car_temp)

Car.set_tax()
#Car.set_tax_regular()

print(f"The tax is: {Car.tax}")
print(f"The price after the tax is: {car_2.GetValue()}")
print(car_3.brand, car_3.model, car_3.founded_year, car_3.price)

print(car_3.check_price(car_3.price))
print(Car.check_price(car_3.price))
    
