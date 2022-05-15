#!/usr/bin/python

import sys
from collections import OrderedDict

class EulerCode:

    def __init__(self):
        self.multiples = []
        max5 = self.find_closest_ceiling(5, 1000)
        max3 = self.find_closest_ceiling(3, 1000)
        self.find_multiples(5, max5)
        self.find_multiples(3, max3)
        self.multiples = list(OrderedDict.fromkeys(self.multiples))

    def find_closest_ceiling(self, multiple, max):
        #Store a temp for the original max
        og_max = max
        #Find the closest number to max which is a multiple
        while(max%multiple != 0):
            max = max - 1
        #If the max is the original value, we have to make sure to exclude it from our count
        if(max == og_max):
            return (max - multiple)
        else:
            return max

    def find_multiples(self, multiple, max):
        while(max != 0):
            self.multiples.append(max)
            max = max - multiple
        
    def add_multiples(self):
        sum = 0
        for val in self.multiples:
            sum = sum + val
        return sum

    def main(self):
        print("The sum is", self.add_multiples())

if __name__ == "__main__":
    e = EulerCode()
    e.main()