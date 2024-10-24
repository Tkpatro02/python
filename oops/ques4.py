class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def Full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Diesel or Petrol"
    
class ElectricCar(Car):
    def __init__(self, brand,model,Battery_Size):
        super().__init__(brand, model)
        self.Battery_Size=Battery_Size

    def fuel_type(self):
        return "Electeric Charge"  

safari=Car("tata","Nexon")
print(safari.fuel_type())

tesla=ElectricCar("tesla","Lx332","887KW")
print(tesla.fuel_type())
# my_car=Car("Hyundai","Creata")
# # print(my_car.brand)
# # print(my_car.model)
# print(my_car.Full_name())

# my_car_new=Car("Mercedes","Lx44W")
# # print(my_car_new.brand)
# # print(my_car_new.model)
# print(my_car_new.Full_name())