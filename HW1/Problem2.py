#!/usr/bin/python3
import math
n = 21
# Your code should be below this line
if n>1 or n<31:
    if n%7==1 or n%7==2:
        print("Weekend")
    else:
        print("Weekday") 
else:
    print("Not valid")