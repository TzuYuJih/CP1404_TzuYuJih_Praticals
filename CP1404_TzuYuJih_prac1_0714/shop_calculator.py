num_of_items = int(input("Number of items: "))
for i in range (num_of_items):
    price_of_item = float(input("Price of item: "))
    price_of_item += price_of_item
print("Total price for {} items is ${}".format(num_of_items,price_of_item))