# """
# CP1404/CP5632 - Practical
# Answer the following questions:
# 1. When will a ValueError occur?
# 2. When will a ZeroDivisionError occur?
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# """
#
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

# Q1. ValueError occurs when I enter something which is not a valid number, such as "q"
# Q2. ZeroDivisionError occurs when the denominator is 0
# Q3. I think I can do that

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can't be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")