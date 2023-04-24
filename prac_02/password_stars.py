def main():
    minimum_length = set_minimum_length()
    password = get_password()
    while len(password) < minimum_length:
        print("Your password doesn't meet a minimum length, please try again!")
        password = get_password()
    print("*" * len(password))


def set_minimum_length():
    length = int(input("Set the minimum length: "))
    return length


def get_password():
    password = str(input("Enter your password: "))
    return password


main()

