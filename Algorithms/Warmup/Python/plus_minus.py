#!/bin/python3

import os
import sys

def plusMinus(arr):
    # Array to store number of positive, negative and zero elements
    # num_el[0] : number of positive elements
    # num_el[1] : number of negative elements
    # num_el[2] : number of zero elements
    num_el = [0, 0, 0]
    
    for x in arr:
        if x > 0:
            num_el[0] = num_el[0] + 1
        elif x < 0:
            num_el[1] = num_el[1] + 1
        else:
            num_el[2] = num_el[2] + 1
          
    # f in print : formatted string literal
    print((f'{num_el[0]/len(arr):.6f}'))
    print((f'{num_el[1]/len(arr):.6f}'))
    print((f'{num_el[2]/len(arr):.6f}'))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)