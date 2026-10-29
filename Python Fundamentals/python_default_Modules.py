# Python have some default modules that are available for use without the need for installation. These modules provide various functionalities and can be imported into your Python programs. Some commonly used default modules include:

# Random Module : 

import random as rd

random_Number = rd.randint(1, 100)
print(f"Random number between 1 and 100 is : {random_Number}")

# Datetime Module :

import datetime as dt
today = dt.date.today()
print(f"Today's date is : {today}")

current_time = dt.datetime.now()
print(f"Current time is : {current_time}")

# Math Module :

import math as mt

def calculate_circle_area(radius):
    area = mt.pi * (radius ** 2)
    return area
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {calculate_circle_area(radius)}")