DISCOUNT = 0.1
DISCOUNT_PRICE = 100   # Discount when the price exceeds $100.
total_price = 0


number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items")
    number = int(input("Number of items: "))

for i in range(number):
    price = float(input("Price of item: "))
    total_price += price

if total_price >= DISCOUNT_PRICE:
    discounted_price = total_price * DISCOUNT
    final_price = total_price - discounted_price
# if total > 100:
    # total *= 0.9
    print(f"Total price for {number} items is ${final_price:,.2f}")




