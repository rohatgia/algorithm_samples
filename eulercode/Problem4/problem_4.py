#!/usr/bin/python

import sys

largest = 0
for x in reversed(range(100,1000)):
    for y in reversed(range(100,1000)):
        mulStr = str(x*y)
        if(mulStr[0:3] == mulStr[3:6][::-1]):
            print(x, y, mulStr)
            if (x*y > largest):
                largest = x*y

print(largest)