#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    result = 0
    
    for x in ar:
        result = result + x    

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()