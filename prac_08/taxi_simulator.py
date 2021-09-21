from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import  Silver_taxi
def main():
    current_Taxi = None
    current_Taxi_num = 0
    bill = 0
    taxis = [Taxi("Pirus", 100), Silver_taxi("Limo", 100, 2), Silver_taxi("Hummer", 200, 4)]
    print("Let's Drive!\n"
          "q)uit, c)hoose taxi, d)rive")
    user_choose = str(input(">>> ")).lower()
    while user_choose != "q":
        if user_choose == "d":
            if current_Taxi:
                current_Taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_Taxi.drive(distance)
                cost = current_Taxi.get_fare()
                print("Your {} trip cost you {}".format(current_Taxi.name, cost))
                bill += cost
                print("Bill to date: $ {}".format(bill))
            else:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: $ {}".format(bill))
        elif user_choose == "c":
            print("Taxi available: ")
            current_Taxi_num = 0
            for i in taxis:
                print("{} - {}".format(current_Taxi_num, i))
                current_Taxi_num += 1
            choose_taxi = int(input("Choose Taxi: "))
            try:
                current_Taxi = taxis[choose_taxi]
                print("Bill to date: $ {}".format(bill))
            except IndexError:
                print("Invalid Taxi Choice")
                print("Bill to date: $ {}".format(bill))

        else:
            print("Invalid Option")
        user_choose = str(input("q)uit, c)hoose taxi, d)rive \n>>> ")).lower()
    print("Total Trip Cost: $ {}".format(bill))

main()