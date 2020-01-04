#https://www.hackerrank.com/challenges/counting-valleys

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valleyCount = 0

    for step in s:
        if step=='U':
            height += 1
        elif height == 0:
            valleyCount += 1
            height -= 1
        else:
            height -= 1

    return valleyCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
