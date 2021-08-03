def main():
    password_limit = 5
    password = get_password()
    if len(password) < password_limit :
        print("Error : Your password length doesn't meet the minimum")
    else:
        print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print('*', end='')


def get_password():
    password = str(input('Please enter your password: '))
    return password


main()