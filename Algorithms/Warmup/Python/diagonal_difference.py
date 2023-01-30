#!/bin/python3

import os
import sys

def diagonalDifference(arr):
    sum_a = 0
    sum_b = 0
    y = n - 1
    
    for x in range(0, n):
        sum_a = sum_a + arr[x][x]
        sum_b = sum_b + arr[x][y]
        y = y - 1
       
    if (sum_a - sum_b) < 0:
        return (sum_a - sum_b) * -1
    else:
        return sum_a - sum_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
