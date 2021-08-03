password_limit = 5
password = str(input('Please enter your password: '))
if len(password) < password_limit :
    print("Error : Your password length doesn't meet the minimum")
else:
    for i in range (len(password)) :
        print('*', end='')
