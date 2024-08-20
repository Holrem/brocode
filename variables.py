## Variables = A container for a value (string, integer, float, boolean)
## A variable behaves as if it was the value it contains

#strings
first_name = "Holrem"
food = "pizza"
email = "fake@fake.com"
print(f"Hi my name is {first_name}, my favorite food is {food} and my email is {email}")

#integers
age = 37
quantity = 3
num_of_students = 30
print(f"I'm {age} years old")
print(f"I'm buying {quantity} items")
print(f"My class has {num_of_students} students")

#float
price = 10.99
gpa = 3.0
distance = 2.5
print(f"The price is ${price}")
print(f"My gpa is {gpa}")
print(f"you ran {distance} miles")

#Boolean
is_student = True
for_sale = False
if is_student:
    print("You are a student")
else:
    print("You are not a student")
if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")