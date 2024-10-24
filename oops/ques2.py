class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def Full_name(self):
        return f"{self.brand} {self.model}"

my_car=Car("Hyundai","Creata")
# print(my_car.brand)
# print(my_car.model)
print(my_car.Full_name())

my_car_new=Car("Mercedes","Lx44W")
# print(my_car_new.brand)
# print(my_car_new.model)
print(my_car_new.Full_name())