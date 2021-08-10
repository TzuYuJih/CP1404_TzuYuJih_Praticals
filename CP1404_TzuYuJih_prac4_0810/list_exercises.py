numbers = [0, 0, 0, 0, 0]
numbers[0] = int(input("Please enter the first number: "))
numbers[1] = int(input("Please enter the second number: "))
numbers[2] = int(input("Please enter the third number: "))
numbers[3] = int(input("Please enter the fourth number: "))
numbers[4] = int(input("Please enter the fifth number: "))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

print("------------")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

ask_username = str(input("Please enter your name: "))
if ask_username in usernames:
    print("Access granted")
else:
    print("Access denied")

