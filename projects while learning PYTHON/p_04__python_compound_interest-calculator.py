#project no 4 : Python Compound Interest Calculator

'''
formula
A = principle * pow((() 1 + rate / 100), time)
'''
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount can't be less or equal to 0.")
    else:
        break

print()

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less or equal to 0.")
    else:
        break

print()

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less or equal to 0.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years is: {total:.2f}$ ")