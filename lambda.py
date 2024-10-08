# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Helps keep the namespace clean and is useful with igher order functions
#                   sort(), map(), filter(), reduce()
#                   lambda parameters: expression


double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
print(max_value(6, 5))

full_name = lambda first, last: first + " " + last
print(full_name("Holrem", "Grinn"))

is_even = lambda x: x % 2 == 0
print(is_even(7))

age_check = lambda age: True if age >= 18 else False
print(age_check(21))