from prac_08.silver_service_taxi import Silver_taxi
def main():
    silver_taxi = Silver_taxi("Hummer", 200, 4)
    print(silver_taxi)
    silver_taxi_2 = Silver_taxi("Test", 100, 2)
    silver_taxi_2.drive(18)
    print(silver_taxi_2.get_new_fare())
main()