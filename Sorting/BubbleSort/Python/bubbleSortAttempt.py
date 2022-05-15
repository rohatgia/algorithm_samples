#!/usr/bin/python

import sys

class bubbleSortAttempt:

    unsorted_array = []

    def __init__(self):
        if(len(sys.argv) > 1):
            self.unsorted_array = sys.argv[1].split(",")