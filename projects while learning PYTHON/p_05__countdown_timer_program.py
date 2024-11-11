#project no 5 : Countdown Timer Program

''''
formula
seconds = num % 60
minutes = (num / 60) % 60
hour = num / 3600
'''

import time

my_time = int(input("Enter a value for time: "))

for x in range(my_time, 0 , -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)
