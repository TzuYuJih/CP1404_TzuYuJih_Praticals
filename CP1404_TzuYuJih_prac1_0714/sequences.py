print("Welcome to the Learning Helper! I can help you to learn about various number sequences!")
value_of_x = int(input("Please enter the value of x: "))
value_of_y = int(input("Please enter the value of y: "))
menu = str(" i. Show the even numbers from x to y\n ii. Show odd numbers from x to y"
           "\n iii. Show the squares from x to y\n iv. Exit the program")
print(menu)
choice = input("Please select your choice (in Roman numerals): ").lower()
while choice != "iv":
    if choice == "i":
        for i in range (value_of_x+1, value_of_y+1, 2):
            print(i, end=" ")
    elif choice == "ii":
        for i in range (value_of_x, value_of_y, 2):
            print(i, end=" ")
    elif choice == "iii":
        for i in range (value_of_x, value_of_y+1):
            print(i*i, end=" ")
    else:
        print("Invalid choice")
    print()
    menu = str(" i. Show the even numbers from x to y\n ii. Show odd numbers from x to y"
               "\n iii. Show the squares from x to y\n iv. Exit the program")
    print(menu)
    choice = input("Please select your choice (in Roman numerals): ").lower()
print("See You :)")
