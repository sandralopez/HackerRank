#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
	# In Python 3 an integer variable is equivalent to long variable in Python 2
	# In Python 2 an integer variable is equal to the machine word length (at least 32 bits). Long is unlimited
    result = 0
    
    for x in ar:
        result = result + x
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()