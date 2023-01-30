#!/bin/python3

import os
import sys

def compareTriplets(a, b):
    points = [0, 0]
    
    for x in range(0, len(a)):
        if a[x] > b[x]:
            points[0] = points[0] + 1
        elif a[x] < b[x]:
            points[1] = points[1] + 1
        
    return points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()