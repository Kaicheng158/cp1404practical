"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * HIGH_BONUS_RATE
    else:
        bonus = sales * LOW_BONUS_RATE
    print(f"you get final bonus of ${bonus}")
    sales = float(input("Enter sales: $"))
print("Next thing will coming!")


