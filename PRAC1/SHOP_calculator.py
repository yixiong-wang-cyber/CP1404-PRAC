DISCOUNT_RATE = 0.9
DISCOUNT_THRESHOLD = 100



total_price = 0.0

number_of_items = int(input("input the number of items: "))

while number_of_items < 0:
    print("invalid number")
    number_of_items = int(input("input the number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("enter the price of the item: "))
    total_price = total_price + price_of_item

if total_price > DISCOUNT_THRESHOLD:
     total_price = total_price * DISCOUNT_RATE

print(f"Total price for {number_of_items} items is ${total_price:.2f}")