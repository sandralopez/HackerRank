#!/bin/python3

import os
import sys

def staircase(n):
    for x in range(1, n+1):
        for y in range(n, x, -1):
            print(" ", end="", flush=True)
        
        for y in range(x, 0, -1):
            print("#", end="", flush=True)
        
        print('')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)