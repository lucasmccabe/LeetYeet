#https://www.hackerrank.com/challenges/30-arrays

import math
import os
import random
import re
import sys

def reverse_arr(arr):
    return arr[::-1]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    output = ''
    for el in reverse_arr(arr):
        output+=str(el)+' '
    
    print(output)