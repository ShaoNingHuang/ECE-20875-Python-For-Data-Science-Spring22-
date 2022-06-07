#!/usr/bin/python3
import math
number = 100
# Your code should be below this line
def is_perfectsquare(num):
    root=math.sqrt(num)
    if int(root)*int(root)==num:
        return 1
    else:
        return 0
if (number%2==0) and (number>=0):
    if is_perfectsquare(5*number*number+4) or is_perfectsquare(5*number*number-4):
        print("Yes")
    else:
        print("No")
else:
    print("NO")