name=str(input("Enter name: "))
menu = str("(H)ello\n(G)oodbye\n(Q)uit")
print(menu)
choice = str(input(">>> "))
while choice != "Q" :
    if choice == "H" :
        print("Hello, {}".format(name))
    elif choice == "G" :
        print("Goodbye, {}".format(name))
    else:
        print("Invalid Choice")
    choice = str(input(">>> "))
print("Finished")