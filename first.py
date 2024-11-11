#############################################
#Lesson 1: This is my first python program
'''
print("I like snow!")
print("It's really good!")
'''

####################################################################
#Lesson 2: Variable
#Variable = A container for a value (string, integer, float, boolean)
#           A variable behaves as if it was the value it contains


#String
first_name = "Violet"
food = "cake"
email = "snow1234@none.com"
'''
print("first_name")
print(first_name)
print(f"Hello {first_name}")
print(f"I like {food}")
print(f"My email is: {email}")
'''

#Integer
age = 29
quantity = 4
num_of_student = 45
'''
print(f"Your age is {age}")
print(f"I have {quantity} of pokemon card")
print(f"Your class has {num_of_student} students")
'''

#Float
price = 10.99
gpa = 3.4
distance = 5.5
'''
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"Your ran {distance}km")
'''

#Boolean
is_student = False
for_sale = True
is_online = True
'''
if is_student:
    print("You are a student.")
else: 
    print("You are not a student.")

if for_sale:
    print("This item is for sale.")
else:
    print("That item is not available.")

if is_online:
    print("You are online.")
else:
    print("You are offline.")
'''


''' Exercise'''
user_name = "Violet Evergarden"
year = 2024
pi = 3.14
is_admin = False

'''
print(f"My favorite character is {user_name}")
print(f"This is {year}")
print(f"The value of pi is {pi}")
if is_admin:
    print("You are a admin.")
else:
    print("You are not an admin.")
'''

#########################################################################################
#Lesson 3: Typecasting = the process of converting a variable from one data type to another  #                        str(), int(), float(), bool()
# specially useful in case of user input
'''
name = "Violet Evergarden"
name_2 = ""
age = 18
gpa = 3.4
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))

age += 1
print(age)


name = bool(name)
print(name)

name_2 = bool(name_2)
print(name_2)
'''

###############################################################################################
#Lesson 4: input() = A function that prompts the user to enter data Returns the entered data as a string
'''
#input() or
name = input("What's your name?: ")
age = int(input("How old are you?: ")) #doing the typecast

#age = int(age) + 1 alternative
age += 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")
'''

#Exercise 1 Rectangle Area Calc
'''
length = input("Enter the value of Rectangular length: ")
width = input("Enter the value of Rectangular width: ")
area = float(length) * float(width)

print(f"The area of the Rectangular is: {area}cm^2")
#for superscript -->  NumLock + Alt + 0178 --> cm^2
'''

#Exercise 2 Shopping Cart Program
'''
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} X {item} / s")
print(f"Your total purchase is ${total}")
'''

########################################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 5: Madlibs game
#word game where you create a story by filling in blanks with random words

'''
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective3} and {verb1}")
print(f"I was {adjective3}!")
'''

################################################################
#Lesson 6: Arithmetic and math
#Arithmetic operators: +, -, *, /, % (modulus), ** (exponent
#Math functions: abs(), round(), pow(), sqrt(), max(), min(), sum()
#Math constants: pi, e


#arithmetic operator
'''
friends = 5

friends = friends + 1
friends += 1

friends = friends - 2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends = friends ** 2
friends **= 2

remainder = friends % 3


print(friends)
print(remainder)
'''

#built in math related function
'''
x = 3.14
y = -4
z = 5

result1 = round(x)
result2 = abs(y)
result3 = pow(4, 2)
result4 = max(x, y, z)
result5 = min(x, y, z)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
'''

#math constant
'''
import math

x = 9

print(math.pi)
print(math.e)
result1 = math.sqrt(x)
result2 = math.ceil(x)
result3 = math.floor(x)

print(result1)
print(result2)
print(result3)
'''

#Exercise
'''
import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is {round(circumference, 2)}cm")
print(f"The area is {round(area, 3)}cm^2")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is {round(c, 2)}")
'''

##############################################
#Lesson 7: If statement
# if = Do some code only IF some condition is True
# Else = Do something else

'''
age = int(input("Enter your age: "))

if age >= 100:
    print("Your too old to sign up.")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up.")
 



response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")


name = input("Enter you name: ")

if name == "":
    print("You did not type you name!")
else:
    print("Hello {name}!")


for_sale = True
if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")


online = False
if online:
    print("The user is online")
else:
    print("The user is offline.")
'''


################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 8: Python Calculator
'''
operator = input("Enter an operator (+, -, *, /): ")

num_1 = float(input("Enter the 1st number: "))
num_2 = float(input("Enter the 2nd number: "))

if operator == "+":
  result = num_1 + num_2
  print(f"The sum is: {result}")
elif operator == "-":
  result = num_1 - num_2
  print(f"The subtraction is: {result}")
elif operator == "*":
  result = num_1 * num_2
  print(f"The multiplication is: {result}")
elif operator == "/":
  result = num_1 / num_2
  print(f"The division is: {round(result, 3)}")
else:
  print(f"{operator} is not valid operator.")
'''

############################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 9: Python weight conversion program
'''
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
  weight = weight * 2.205
  unit = "Lbs."
  print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
  weight = weight / 2.205
  unit = "Kgs."
  print(f"Your weight is: {round(weight, 1)} {unit}")
else:
  print(f"{unit} is not valid.")
'''

###############################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 10: Temperature conversion program
# Alt + 0176 = °

'''
temp = float(input("Enter temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")


if unit == "C":
  temp = round((temp * 9) / 5 + 32 , 1)
  print(f"The temperature in Fahrenheit is: {temp} °F")
elif unit == "F":
  temp = round((temp - 32) * 5 / 9 , 1)
  print(f"The temperature in Celsius is: {temp} °C")
else:
  print(f"{unit} is not a valid measurement.")
'''


#Lesson 11: Logical Operator
'''
logical operator = evaluate multiple conditions (or, and, not)
or = at least one condition must be True
and = both condition must be True
not = inverts the condition (not False, not True)
'''

# or logical operator
'''
temp = 50
is_raining = False

if temp > 35 or temp < 0 or is_raining:
  print("The outdoor event is cancelled")
else:
  print("The outdoor event is still scheduled")
'''

# and logical operator
'''
temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
  print("It is Hot outside 🥵.")
  print("It is sunny 🌞.")
elif temp <= 0 and is_sunny:
  print("It is cold outside🥶.")
  print("It is sunny 🌞.")
#elif temp < 28 and temp < 0 and is_sunny:  or
elif 28 > temp > 0 and is_sunny:
  print("It is warm outside😃.")
  print("It is sunny 🌞.")
'''

# not logical operator
'''
temp = 20
is_sunny = False

if temp >= 28 and not is_sunny:
  print("It is Hot outside 🥵.")
  print("It is cloudy ☁️.")
elif temp <= 0 and not is_sunny:
  print("It is cold outside🥶.")
  print("It is cloudy ☁️.")
#elif temp < 28 and temp < 0 and is_sunny:  or
elif 28 > temp > 0 and not is_sunny:
  print("It is warm outside😃.")
  print("It is cloudy ☁️.")
'''

#################################################
#Lesson 12: Conditional expression
'''
#conditional expression = A one-line shortcut for the if-else statement (Ternary operator)
#                        Print or assign one of two values based on a condition
#                       X if condition else Y (means if x true return or else return y)
'''
'''
num = 6
a = 6
b = 7
age = 13
temperature = 45
user_role = "Admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "Admin" else "Limited access"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)
'''

##################################
#Lesson 13: String methods
# len(), find(), rfind(), capitalize(), upper(), lower(), isdigit(), isalpha(), count(), replace("", "")

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

'''
result_1 = len(name)
result_2 = name.find("e")  # 1st occurrence function
result_3 = name.rfind("e")  #last occurrence function
result_4 = name.rfind("0")
result_5 = name.capitalize()
result_6 = name.upper()
result_7 = name.lower()
result_8 = name.isdigit()
result_9 = name.isalpha()
result_10 = phone_number.count("-")
result_11 = phone_number.replace("-", " ")

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
print(result_7)
print(result_8)
print(result_9)
print(result_10)
print(result_11)
'''

#extra function
#print(help(str))

#Exercise 
'''
validate user input exercise
1. username is no more than 12 characters
2. username must not contain spaces
3. username must not contain digits
'''

'''
user_name = input("Enter a valid user name: ")


if len(user_name) > 12:
  print("Your user name can't be more than 12 character.")
elif user_name.find(" ") != -1:
  print("User name can't contain any spaces.")
elif not user_name.isalpha() :
  print("User name can't contain any digit.")
else:
  print(f"{user_name} WELCOME!!")
'''

##################################################
#Lesson 14: String indexing
'''
indexing = accessing elements of a sequence using [] indexing operator [start : end : step]
'''

'''
credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])

last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

#reverse the string with negative number
credit_number = credit_number[::-1]
print(f"The reverse string is: {credit_number}")
'''

##################################################
#Lesson 15: Format Specifiers
'''
format specifiers = {value:flags} format a value based on what flags are inserted

.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate positive value
:= = place sign to leftmost position
:  = insert a space before positive numbers
:, = comma separator

'''

'''
price_1 = 3353.14159
price_2 = -9487.65
price_3 = 12536.34

print(f"Price 1 is ${price_1: .2f}")
print(f"Price 2 is ${price_2: 10}")
print(f"Price 3 is ${price_3:010}")

print(f"Price 1 is ${price_1:<10}")
print(f"Price 2 is ${price_2:>10}")
print(f"Price 3 is ${price_3:^10}")

print(f"Price 1 is ${price_1:+}")
print(f"Price 2 is ${price_2: }")
print(f"Price 3 is ${price_3: }")

print(f"Price 1 is ${price_1:,}")
print(f"Price 2 is ${price_2:+,.2f}")
'''

###################################################
#Lesson 16: While loops
#execute some code WHILE some condition remains true

'''
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"Your like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")

num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
'''

#####################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 17:Python Compound Interest Calculator
'''
principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")


total = principle * pow( (1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
'''

#alternative ways to write this program is
'''
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break


total = principle * pow( (1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
'''

######################################################
#Lesson 18: For loops
#execute a block of code a fixed number of times. You can iterate over a range, string, sequence etc

'''
for x in range(1, 11):
  print(x)

print("Happy birthday")

for counter in reversed(range(1, 11)):
  print(counter)

print("Happy birthday")

for x in range(1, 11, 3):
  print(x)

#for string
credit_number = "1234-5678-9012-3456"

for x in credit_number:
  print(x)


for x in range(1, 10):
  if x == 6:
    continue
  else:
    print(x)

for x in range(1, 10):
  if x == 6:
    break
  else:
    print(x)
'''

#########################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 19: Countdown timer program
'''
import time

time.sleep(3)
print("Time's up!")


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
  seconds = x % 60
  minutes = int(x / 60) % 60
  hours = int(x / 3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
'''

#########################################################
#Lesson 20: Nested loops
'''
A loop within another loop (outer, inner)
        outer loop:
            inner loop:
'''
'''
for x in range(3):
  for y in range(1, 11):
    print(y , end=" ")
  print()

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
  for y in range(columns):
    print(symbol, end="")
  print()
'''

#########################################################
#Lesson 21: Lists, Sets, Tuples
'''
Collection = single "variable" used to store multiple values
List = [] ordered and changeable. Duplicates OK
Set = {} unordered and immutable, but Add/Remove OK. NO duplicated
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
Dictionary next time...
'''

# ----------> List

'''
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

print(fruits[::-1])

for fruit in fruits:
  print(fruit)
 
# what list function can do (attributes)
#print(dir(fruits))
# description of all the attributes and methods
#print(help(fruits))

print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.remove(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.count("banana"))
print(fruits.index("apple"))

for fruit in fruits:
  print(fruit)
'''

# ----------> Set
'''
fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# what list function can do (attributes)
#print(dir(fruits))
# description of all the attributes and methods
#print(help(fruits))

print(len(fruits))
print("apple" in fruits)

#can't use indexing
fruits.add("watermelon")
fruits.remove("apple")
fruits.pop()
#fruits.clear()

print(fruits)
'''
# ----------> Tuple
'''
fruits = ("apple", "orange", "banana", "coconut", "coconut")

# what list function can do (attributes)
#print(dir(fruits))
# description of all the attributes and methods
#print(help(fruits))

print(len(fruits))
print("apple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
  print(fruit)
'''


####################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 22: Shopping Cart Program
'''
foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy (q to buy): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of a {food}: $"))
    foods.append(food)
    prices.append(price)


print("-------Your Cart-------")

for food in foods:
  print(food, end = " ")

for price in prices:
  total += price

print()
print(f"Your total is : ${total}")
'''

######################################################
#Lesson 23: 2D Collection
# 2D list = [list_1, list_2, list_3]

'''
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
#or

#2D list
#groceries = [ ["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turkey"]
#            ]

#2D tuple
#groceries = ( ("apple", "orange", "banana", "coconut"),
#              ("celery", "carrots", "potatoes"), 
#              ("chicken", "fish", "turkey")
#            )

#tuple made of sets
#groceries = ( {"apple", "orange", "banana", "coconut"},
#              {"celery", "carrots", "potatoes"}, 
#              {"chicken", "fish", "turkey"}
#            )

print(groceries[0][1])

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()


#-----Exercise
num_pad = ( (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#")
          )

for column in num_pad:
  for row in column:
    print(row, end=" ")
  print()

'''

############################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
# Lesson 24: Python quiz game
'''
questions = ( "How many elements are in the periodic table?: ",
              "Which animal lays the largest eggs?: ",
              "What is the most abundant gas in the Earth's atmosphere?: ",
              "How many bones are in the human body?: ",
              "Which planet in the solar system is the hottest?: "
            ) 

options = ( ("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
          )

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("-------------------------")
  print(question)

  for option in options[question_num]:
    print(option, end = " ")


  guess = input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)

  if guess == answers[question_num]:
    score += 1
    print("CORRECT!!")
  else:
    print("INCORRECT!!")
    print(f"The {answers[question_num]} is the correct answer.")

  question_num += 1



print("-------------------------")
print("         Result          ")
print("-------------------------")

print("answers: ", end=" ")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
  print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")

'''
###################################################
#Lesson 25: Dictionary
# a collection of {key: value} pairs ordered and changeable. No duplicates
'''
capitals = {"USA": "Washington D.C.",
          "India": "New Delhi",
          "China": "Beijing",
          "Russia": "Moscow"}


#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))

if capitals.get("Russia"):
  print("That capital exists.")
else:
  print("That capital doesn't exists.")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()



print(capitals)

#keys
keys = capitals.keys()
print(keys)

for key in capitals.keys():
  print(key)

#values
values = capitals.values()
print(values)

for value in capitals.values():
  print(value)

#items = [(), (), ()]
items = capitals.items()
print(items)

for key, value in capitals.items():
  print(f"{key}: {value}")
'''

################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 26: Concession stand program
'''
menu = {"pizza": 3.00, 
        "nachos": 4.50, 
        "popcorn": 6.00, 
        "fries": 2.50, 
        "chips": 1.00, 
        "pretzel": 3.50, 
        "soda": 3.00, 
        "lemonade": 4.25}

cart = []
total = 0

print("----------MENU----------")
for key, value in menu.items():
  print(f"{key:10}: ${value:.2f}")
print("-------------------------")

while True:
  food = input("Select an item (q to quit): ").lower()

  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)

print(cart)


print("_______YOUR ORDER_______")
for food in cart:
  total += menu.get(food)
  print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
'''

##################################################
#Lesson 27: Random numbers
'''
import random

low = 1
high = 100


options = ("rock", "paper", "scissors")
#number = random.randint(low, high)
#number = random.random()
#print(number)

#option = random.choice(options)
#print(option)

cards = ["2", "3", "4","5" ,"6" , "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
'''


##########################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 28: Python Number guessing game
'''
import random


lowest_num = 1
hightest_num = 100
answer = random.randint(lowest_num, hightest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game.")
print(f"Select a number between {lowest_num} and {hightest_num}")

while is_running:
  
  guess = input("Enter you guess: ")

  if guess.isdigit():
    guess = int(guess)
    guesses += 1
    if guess < lowest_num or guess > hightest_num:
      print("That number is out of range.")  
      print(f"Select a number between {lowest_num} and {hightest_num}")
    elif guess < answer:
      print("Too low! Try again!!!")
    elif guess > answer:
      print("Too high! Try again!!!")
    else:
      print(f"CORRECT! The answer was {answer}")
      print(f"Number of guesses: {guesses}")
      is_running = False

  else:
    print("Invalid guess!!")
    print(f"Select a number between {lowest_num} and {hightest_num}")
'''

#########################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
#Lesson 29:Rock, Paper, Scissor game
'''
import random

options = ("rock", "paper", "scissor")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter a choice (rock, paper, scissor): ")

  print(f"Player: {player}")
  print(f"Computer: {computer}")

  if player == computer:
      print("It is a tie!")
  elif player == "rock" and computer == "scissor":
      print("You WIN!!!")
  elif player == "paper" and computer == "rock":
      print("You WIN!!!")
  elif player == "scissor" and computer == "paper":
      print("You WIN!!!")
  else:
      print("You LOOSE!!!")
    
  if not input("Play again? (y/n):").lower() == "y":
      running = False

  
print("Thanks for playing!")
'''

########################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
# Lesson 30: Dice Roller Program
'''

import random

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {

  1 : ( "┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
  2 : ( "┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
  3 : ( "┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
  4 : ( "┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
  5 : ( "┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
  6 : ( "┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")

}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
  dice.append(random.randint(1, 6))

for line in range(5):
  for die in dice:
    print(dice_art.get(die)[line], end="")
  print()

for die in dice:
  total += die
print(f"Total: {total}")

'''

##################################################
# Lesson 31: Functions
# A block of reusable code place () after the function name in invoke in

'''
def happy_birthday_song(name, year):
  print(f"Happy Birthday to {name}.")
  print(f"You are {year} yeats old.")
  print("Happy birthday to you.")

happy_birthday_song("Shimu", 21)
print()
happy_birthday_song("Dalia", 21)
print()

def display_invoice(username, amount, due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Violet", 42.30, "01/01/2024")
print()


#----return = statement used to end a function and send a result back to the caller

def addition(x, y):
  z = x + y
  return z

def subtraction(x, y):
  z = x - y
  return z

def multiplication(x, y):
  z = x * y
  return z

def division(x, y):
  z = x / y
  return z

print(addition(3, 5))
print(subtraction(45, 10))
print(multiplication(4, 5))
print(division(4, 2))


def create_name(first, last):
  first = first.capitalize()
  last = last.capitalize()
  return first + " " + last

full_name = create_name("violet", "evergarden")
print(full_name)
'''

#################################################
# Lesson 32: Default Arguments
'''
A default a value for certain parameters default is used when that argument is omitted
make your functions more flexible, reduces 
# of arguments 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
'''

'''
def net_price(list_price, discount = 0, tax = 0.05):
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

#-----Exercise ... for countdown

import time

def count(end, start=0):
  for x in range(start, end+1):
    print(x)
    time.sleep(1)
  print("DONE!")

count(30, 15)
'''

#############################################
# Lesson 33: Keyword Arguments
'''
An argument preceded by an identifier helps with readability order of arguments doesn't matter 
1. positional, 2. default, 3. KEYWORD, 4. arbitrary
'''

'''
def hello(greeting, title, first, last):
  print(f"{greeting} {title}{first} {last}")

hello("Hello!", title = "Mr.", last = "Squarepants", first = "Spongebob")

for x in range(1, 11):
  print(x, end=" ")

print("1", "2", "3", "4", "5", sep="-")

#----Exercise

def get_phone(country, area, first, last):
  return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
'''

#######################################################
# Lesson 34: Args and Kwargs --> Arbitrary Arguments
'''
*args = allows you to pass multiple non-key arguments
**kwargs = allows you to pass multiple key arguments
* unpacking operator
1. positional, 2. default, 3. keyword, 4. ARBITRARY
'''

#...args...
#def add(*args):
#  print(type(args))

'''
def add(*args):
  total = 0
  for arg in args:
    total += arg
  return total


print(add(1, 2, 3))

def display_name(*args):
  for arg in args:
    print(arg, end=" ")
  
display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
'''

#...kwargs...
#def print_address(**kwargs):
#  print(type(kwargs))

'''
def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")


print_address(street = "123 Fake st.", 
              apt = "100",
              city = "Detroit", 
              state = "MI", 
              zip = "54321")


#---Exercise

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")

  print()
  #for value in kwargs.values():
  #  print(value, end=" ")

  if "apt" in kwargs:
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  elif "pobox" in kwargs:
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('pobox')}")
  else:
    print(f"{kwargs.get('street')}")

  print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
                street = "123 Fake st.", 
                #apt = "100"
                pobox = "PO box #1001",
                city = "Detroit", 
                state = "MI", 
                zip = "54321")
'''

#############################################################
# Lesson 35: Iterables
'''
An object/ collection that can return its elements one at a time, allowing it to be iterated over in a loop
'''
'''
#---Example 1: List
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
  print(number, end=" - ")

print()
#---Example 2: Tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
  print(number)

print()
#---Example 3: Sets
fruits = {"apple", "orange", "banana", "coconut", "watermelon"}
for fruit in fruits:
  print(fruit)

#---Example 4: Strings
name = "Bro code"
for character in name:
  print(character, end=" ")

#---Example 5: Dictionary
my_dictionary = {"A": 1, "B": 2, "C": 3,}
for key, value in my_dictionary.items():
  print(f"{key} = {value}")
'''

#############################################################
# Lesson 36: Membership Operators
'''
used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)
1. in (word)
2. not in (word)
'''

'''
#-----Example 1
word = 'APPLE'

letter = input("Guess a letter in the secret word: ")

if letter in word:
  print(f"There is a {letter}.")
else:
  print(f"{letter} was not found.")

if letter in not word:
  print(f"There is a {letter}.")
else:
  print(f"{letter} was not found.")


#-----Example 2
students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter the name of a student: ")

if student in students:
  print(f"{student} is a student.")
else:
  print(f"{student} was not found.")

#-----Example 3
grades = {"Sandy": "A", 
        "Squidward": 
        "B","Spongebob": 
        "C","Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
  print(f"{student}'s grade is {grades[student]}")
else:
  print(f"{student} was not found")


#-----Example 4
email = "BroCode@gmail.com"

if "@" in email and "." in email:
  print("Valid email.")
else:
  print("Invalid email.")

'''

#####################################################
# Lesson 37: List Comprehensions
'''
A concise way to create lists in Python Compact and easier to read than traditional loops [expression for value in iterable if condition]
'''

'''
#traditional loops
double = []
for x in range(1, 11):
  double.append(x * 2)
print(double)

#concise way

doubles = [ x * 2 for x in range(1, 11)]
triples = [ y * 3 for y in range(1, 11)]
squares = [ z * z for z in range(1, 11)]  

print(doubles)
print(triples)
print(squares)

fruits = ["watermelon", "apple", "banana", "coconut", "orange"]
fruits = [ fruit.upper() for fruit in fruits]
print(fruits)

fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)


numbers = [1, 2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

#----Exercise

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]
print(passing_grade)
'''

########################################################
# Lesson 38: Match-case Statement (switch)
'''
An alternative to using many 'elif' statements
Execute some code if a value matches a 'case' Benefits: cleaner and syntax in more readable.
'''

'''
def day_of_week(day):
    if day == 1:
        return "It is Sunday."
    elif day == 2:
        return "It is Monday."
    elif day == 3:
        return "It is Tuesday."
    elif day == 4:
        return "It is Wednesday."
    elif day == 5:
        return "It is Thursday."
    elif day == 6:
        return "It is Friday."
    elif day == 7:
        return "It is Saturday."
    else:
      return "Not a valid day."


print(day_of_week(5))

#---alternative
def day_of_week(day):
    match day:
      case 1:
          return "It is Sunday."
      case 2:
          return "It is Monday."
      case 3:
          return "It is Tuesday."
      case 4:
          return "It is Wednesday."
      case 5:
          return "It is Thursday."
      case 6:
          return "It is Friday."
      case 7:
          return "It is Saturday."
      case _:
        return "Not a valid day."

print(day_of_week(6))


def is_weekend(day):
    match day:
      case "Saturday" | "Sunday":
          return True
      case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
          return False
      case _:
        return False

print(is_weekend("Monday"))
'''

#####################################################
#Lesson 39: Modules 
''' 
A file containing code you want to include in your program use 'import' to include a module (built-in or your own)
useful to break up a large program reusable separate files
'''

'''
#list of modules
#print(help("modules"))
#print(help("math"))

#import math
#import math as m
#from math import pi


#print(math.pi)
#print(m.pi)
#print(pi)

# name conflict for ---- from math import pi
from math import pi
a, b, c, d, e = 1, 2, 3, 4, 5

print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)


# correct way to write it is 
import math

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)


# creating my own new module named "example.py"
import example

result = example.pi
result_1 = example.square(3)
result_2 = example.cube(4)
result_3 = example.circumference(3)
result_4 = example.area(6)

print(result)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
'''

#######################################################
# Lesson 40: Scope resolution
''''
Where a variable is visible and accessible
scope resolution = (LEGB) Local -> Enclose -> Global -> Built-in
order----------------------1st------ 2nd------ 3rd------- 4th 
'''
'''
#local
def func1():
    x = 1
    print(x)

def func2():
    x = 3
    print(x)

func1()
func2()

#enclose
def func1():
    x = 1
    print(x)

    def func2():
        x = 3
        print(x)
    func2()

func1()

#enclose
def func1():
    x = 1
    print(x)

    def func2():
        print(x)
    func2()

func1()

#global --- outside of any function
def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

#built-in

from math import e
def function():
    print(e)

e = 3 
function()
'''

###############################################
# Lesson 41: if name == 'main'
'''
if__name__==__main__: (this script can be imported OR run standalone)
Function and classes in this module can be reused
without the main block of code executing
Good practice ( code is modular, 
                helps readability, 
                leaves no global variables, 
                avoid unintended execution)

example library = Import library for functionality when running directly, display a help page

'''

'''
if __name__=='__main__':
  main()

# we are using three python file for this lesson 
# (script1.py and script2.py and python.py 
# --- for script1.py and script2.py 
# i have modified the run configuration)
'''

##########################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
# Lesson 42: Python Banking Program
'''

def show_balance(balance):
  print("***********************************")
  print(f"Your balance is ${balance:.2f}")
  print("***********************************")


def deposit():
  print("***********************************")
  amount = float(input("Enter an amount to be deposited: "))
  print("***********************************")

  if amount < 0:
    print("***********************************")
    print("That's not a valid amount.")
    print("***********************************")
    return 0
  else:
    return amount


def withdraw(balance):
  print("***********************************")
  amount = float(input("Enter an amount to be withdrawn: "))
  print("***********************************")

  if amount > balance:
    print("***********************************")
    print("Insufficient funds.")
    print("***********************************")
    return 0
  elif amount < 0:
    print("***********************************")
    print("Amount must be greater than 0.")
    print("***********************************")
    return 0
  else:
    return amount

def main():
  balance = 0
  is_running = True

  while is_running:
    print("***********************************")
    print("          Banking Program.         ")
    print("***********************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("***********************************")

    choice = input("Enter your choice (1 - 4): ")

    if choice == '1':
      show_balance(balance)
    elif choice == '2':
      balance += deposit()
    elif choice == '3':
      balance -= withdraw(balance)
    elif choice == '4':
      is_running = False
    else:
      print("***********************************")
      print("That is not a valid choice.")
      print("***********************************")

  print()
  print("***********************************")
  print("Thank you! Have a nice day.")
  

if __name__ == '__main__':
    main()

'''

#####################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
# Lesson 43: Python Slot Machine
# for inserting emoji = win + ;
'''
import random

def spin_row():
  symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

  return [random.choice(symbols) for _ in range(3)]


def print_row(row):
  print("****************")
  print(" | ".join(row))
  print("****************")


def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == '🍒':
      return bet * 3
    elif row[0] == '🍉':
      return bet * 4
    elif row[0] == '🍋':
      return bet * 5
    elif row[0] == '🔔':
      return bet * 10
    elif row[0] == '⭐':
      return bet * 20
    
  return 0
  

def main():
  balance = 100

  print("*************************")
  print("Welcome to Python Slots.")
  print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
  print("*************************")

  while balance > 0:
    print(f"Current balance: ${balance}")

    bet = input("Place your bet amount: ")

    if not bet.isdigit():
      print("Please enter a valid number.")
      continue
  
    bet = int(bet)

    if bet > balance:
      print("Insufficient funds.")
      continue

    if bet <= 0:
      print("Bet must me greater than 0.")
      continue
    
    balance -= bet

    row = spin_row()
    print("Spinning....\n")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
      print(f"You won ${payout}")
    else:
      print("Sorry you lost this round.")

    balance += payout

    play_again = input("Do you want to spin again? (Y/N): ").upper()
    
    if play_again != 'Y':
      break

  print("********************************************")
  print(f"Game Over! Your final balance is ${balance}")
  print("********************************************")


if __name__ == '__main__':
    main()
'''

####################################################
#🐍🔥🐍🔥🐍🔥🔥✨💻🌈🎉🔆🔥🔥🐍🔥🐍🔥🐍
# Lesson 44: Encryption Program

'''
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars: {chars}")
#print(f"Key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = " "

for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]

print(f"original massage: {plain_text}")
print(f"encrypted message: {cipher_text}")


#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = " "

for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]


print(f"encrypted message: {cipher_text}")
print(f"original massage: {plain_text}")
'''
#...........06:07:25




