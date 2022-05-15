#!/usr/bin/python

import sys

#basic approach
fibonacci_nums = [0, 1]
sum = 0
num = fibonacci_nums[-1] + fibonacci_nums[-2]

while(num < 4000000):
    if(fibonacci_nums[-1]%2 == 0):
        sum = sum + fibonacci_nums[-1]
    num = fibonacci_nums[-1] + fibonacci_nums[-2]
    fibonacci_nums.append(num)
    
print(sum)