from prac_06.guitar import guitar
guitar_list = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    new_guitar = guitar(name, year, cost)
    guitar_list.append(new_guitar)
    print("{} ({}) : ${} added".format(name, year, cost))

    name = input("Name: ")


print("There's my guitars:")
guitar_list.append(guitar("Gibson L-5 CES", 1922, 16035.40))
guitar_list.append(guitar("Line 6 JTV-59", 2010, 1512.9))
for i, guitar in enumerate(guitar_list):
    vintage_str = "(vintage)" if guitar.is_vintage() == True else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_str}")

