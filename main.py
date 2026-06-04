from car_class import Car

my_car = Car()

print("Accelerating:")
for i in range(5):
    my_car.accelerate()
    print(f"Current Speed: {my_car.get_speed()}")