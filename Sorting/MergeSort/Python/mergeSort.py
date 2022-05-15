#!/usr/bin/python

import sys, random, copy, time

unsorted_array = []
arr_length = 0

def right_lower(a, b):
    if a > b:
        return True
    else:
        return False

def is_sorted(arr):
    for i in range(0, len(arr) - 1):
        if right_lower(arr[i], arr[i+1]):
            return False
    return True

def split(arr):
    midpoint = len(arr)/2
    #print(midpoint)
    midpoint = int(midpoint)
    arrA = arr[0 : midpoint]
    arrB = arr[midpoint : ]
    return arrA, arrB

def merge(arrA, arrB):
    print(arrA, arrB)
    if len(arrA) > 1:
        arrA1, arrA2 = split(arrA)
        arrA = merge(arrA1, arrA2)
    if len(arrB) > 1:
        arrB1, arrB2 = split(arrB)
        arrB = merge(arrB1, arrB2)
    i = 0
    j = 0
    sorted_arr = []
    total_len = len(arrA) + len(arrB)
    #print(len(sorted_arr), total_len)
    while(len(sorted_arr) != total_len):
        if(i == len(arrA)):
            sorted_arr.append(arrB[j])
            j += 1
        elif(j == len(arrB)):
            sorted_arr.append(arrA[i])
            i += 1
        else:
            print(arrA[i], arrB[j])
            if (arrA[i] < arrB[j]):
                sorted_arr.append(arrA[i])
                i += 1
            elif (arrA[i] > arrB[j]):
                sorted_arr.append(arrB[j])
                j += 1
            elif (arrA[i] == arrB[j]):
                sorted_arr.append(arrA[i])
                i += 1
                sorted_arr.append(arrB[j])
                j += 1
            else:
                print("what")
        #print(len(sorted_arr), total_len)
    print(sorted_arr)
    return sorted_arr

if(len(sys.argv) <= 1):
    arr_length = 10
else:
    print("arr length is", sys.argv[1])
    arr_length = sys.argv[1]
arr_length = int(arr_length)
for i in range(0, arr_length):
    unsorted_array.append(random.randint(0,2*arr_length))

print(unsorted_array)
time1 = time.time()
is_sort = is_sorted(unsorted_array)
if is_sort is False:
    arrA, arrB = split(unsorted_array)
    unsorted_array = merge(arrA, arrB)
print(unsorted_array)