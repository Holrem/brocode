# Exercise 1 Rectangle Area Calc and Shopping cart

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is {area}cm²")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")