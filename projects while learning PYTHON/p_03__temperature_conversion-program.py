#project no 3 : Temperature Conversion Program
'''
formulas Celsius and Fahrenheit

°F = ( 9/5 * °C ) + 32
°C = 5/9 * ( °F - 32 )

'''

temp = float(input("Enter a temperature value: "))
cov = input("Enter which temperature you want to convert: ")

if cov == "F":
    result = ( 9/5 * temp ) + 32
    print(f"Temperature in Fahrenheit: {result}°F")
elif cov == "C":
    result = 5/9 * ( temp - 32 )
    print(f"Temperature in Celsius: {result}°C")
else:
    print(f"Your input {cov} is not valid.")