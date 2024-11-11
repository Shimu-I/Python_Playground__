#project no 2 : python calculator
'''
these operation will be performed
+ - * / 
'''

num_1 = float(input("Enter 1st number: "))
num_2 = float(input("Enter 2nd number: "))
operator = input("Select an operator: ")

if operator == "+":
    result = num_1 + num_2
    print(f"ADDITION: {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"SUBTRACTION: {result}")
elif operator == "*":
    result = num_1 * num_2
    print(f"MULTIPLICATION: {result}")
elif operator == "/":
    result = num_1 / num_2
    print(f"DIVISION: {result}")
else:
    print(f"THe operator {operator} is not valid/")