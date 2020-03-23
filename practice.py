# practicing python coding
import sys
import datetime
import math

print("Python version: " + str(sys.version_info))

now = datetime.datetime.now()

print("current Date: " + now.strftime("%Y-%m-%d %H:%M:%S"))

"""
x = input("Input a radius = ")
y = int(x)*int(x)
print("Circumference = " + str(math.pi * int(y)))
"""

"""
fname = str(input("First name: "))
lname = str(input("Last name: "))
print("Hello, " + lname + " " + fname)
"""