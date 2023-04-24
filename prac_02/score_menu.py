Menu = "(G)et a valid score(must be 0-100 inclusive)\n(P)rint result\n(S)how star\n(Q)uit"


def main():
    print(Menu)
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "P":
            result = check_score(score)
            print(f"Your result is {result}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(Menu)
        choice = get_choice()
    print("Farewell.")


def get_choice():
    answer = input("Enter your choice: ").upper()
    return answer


def get_score():
    number = int(input("Enter score (must be 0-100 inclusive): "))
    return number


def check_score(score):
    if score < 0 or score > 100:
        response = "Invalid score"
    elif score < 50:
        response = "Bad"
    elif score < 90:
        response = "Pass"
    else:
        response = "Excellent"
    return response


main()
