import math

# Part 1 Circumference of a circle
radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")


# Part2 Area of a circle
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")


# Part 3 Hypotenuse of a right triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

