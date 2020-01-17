#https://www.hackerrank.com/challenges/30-binary-numbers/

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_n = str(bin(n)[2:])

    max_ones = '1'*len(bin_n)
    while max_ones not in bin_n:
        max_ones = max_ones[:-1]
    print(len(max_ones))