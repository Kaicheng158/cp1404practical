import random


def main():
    score = get_score()
    response = check_score(score)
    print(response)
    random_score = random.randint(0, 100)
    random_response = check_score(random_score)
    print(f"Random score is {random_score}, and it is {random_response}")


def get_score():
    number = float(input("Enter score: "))
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



