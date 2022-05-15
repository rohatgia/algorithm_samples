#!/usr/bin/python

import sys
from collections import OrderedDict

num = 600851475143
factors = []
factor = 2

while(factor != 0):
    div = num/factor
    if(factor > div):
        break
    if(div.is_integer()):
        print("HIT", factor, div)
        factors.append(factor)
        factors.append(int(div))
    factor = factor + 1

factors.sort()
for x in reversed(factors):
    for y in factors:
        if x == y:
            print("HIT3", x, y)
            break
        div = x/y
        if(div.is_integer()):
            if(int(div) in factors):
                print("Non-Prime", x, y, div)
                break