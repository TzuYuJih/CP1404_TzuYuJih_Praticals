from prac_08.unreliable_car import Unreliable_car

def main():
    test_car = Unreliable_car("Test", 100, 50)
    print("Car name: {}, Fuel: {}, Reliablility: {}".format(test_car.name, test_car.fuel, test_car.reliablility))
    test_car.drive(10)
    if test_car.fuel != 100:
        print("Drive Successfully! Current fuel: {}".format(test_car.fuel))
    else:
        print("Drive Fail! Current fuel: {}".format(test_car.fuel))

main()