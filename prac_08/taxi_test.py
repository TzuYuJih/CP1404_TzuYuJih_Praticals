from prac_08.taxi import Taxi

def main():
    pirus1 = Taxi("Pirus 1", 100)
    pirus1.drive(40)
    print("Taxi name: {}, Current Fuel: {}, Current Fare: {}".format(pirus1.name, pirus1.fuel, pirus1.get_fare()))
    pirus1.start_fare()
    pirus1.drive(100)
    print("Taxi name: {}, Current Fuel: {}, Current Fare: {}".format(pirus1.name, pirus1.fuel, pirus1.get_fare()))

main()