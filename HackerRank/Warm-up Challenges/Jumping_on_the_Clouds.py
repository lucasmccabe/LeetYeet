#https://www.hackerrank.com/challenges/jumping-on-the-clouds/

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if c[0]==0:
        cloudsUsed = [0]
    else:
        cloudsUsed = [1]
    i = cloudsUsed[0]
    while i<len(c):
        #i is cloud currently stationed on
        if i+2<len(c) and c[i+2]==0:
            i += 2
        elif i+1<len(c):
            i += 1
        else:
            break
        cloudsUsed.append(i)
    return len(cloudsUsed)-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
