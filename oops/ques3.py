class Car:
    def __init__(self,brand,model,Battery_Size):
        self.brand=brand
        self.model=model
        self.Battery_size=Battery_Size

    def Full_name(self):
        return f"{self.brand} {self.model} {self.Battery_size} "
    
class ElectricCar(Car):
    def __init__(self, brand,model,Battery_Size):
        super().__init__(brand, model,Battery_Size)
        
    # def Full_name(self):
    #     return f"{self.brand} {self.model} {self.Batter_size} "
my_tesla=ElectricCar("tesla","Evv2","123kW")
print(my_tesla.Full_name())
    
my_car=Car("Hyundai","Creata","32ks")
# print(my_car.brand)
# print(my_car.model)/
print(my_car.Full_name())

my_car_new=Car("Mercedes","Lx44W","32ks")
# print(my_car_new.brand)
# print(my_car_new.model)
print(my_car_new.Full_name())