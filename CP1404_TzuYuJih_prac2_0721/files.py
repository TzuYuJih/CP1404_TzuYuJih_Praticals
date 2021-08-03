# Q1.
users_name= str(input("Please enter your name: "))
out_file_names = open("name.txt", 'w')
print(users_name, file=out_file_names)
out_file_names.close()
print("-------------------")
# Q2.
input_file_names = open("name.txt", "r")
read_the_name = input_file_names.read()
print("Your name is", read_the_name)
input_file_names.close()
print("-------------------")
# Q3.
input_file_numbers = open("numbers.txt", "r")
read_first_line = input_file_numbers.readline()
read_second_line = input_file_numbers.readline()
num1 = int(read_first_line)
num2 = int(read_second_line)
sum = num1 + num2
print('{} + {} = {}'.format(num1, num2, sum))
input_file_numbers.close()
print("-------------------")
# Q4.
total = 0
input_file_numbers = open("numbers.txt", "r")
read_all_line = input_file_numbers.read()
sp = read_all_line.split()
for i in sp:
    total += eval(i)
print(total)
input_file_numbers.close()