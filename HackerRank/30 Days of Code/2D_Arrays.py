#https://www.hackerrank.com/challenges/30-2d-arrays/

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sums = []
    for i in range(4):
        for j in range(4):
            s = sum(arr[i][j:j+3])+\
                arr[i+1][j+1]+\
                sum(arr[i+2][j:j+3])
            sums.append(s)
    print(max(sums))