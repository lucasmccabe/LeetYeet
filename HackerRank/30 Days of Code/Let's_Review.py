#https://www.hackerrank.com/challenges/30-review-loop/

import sys

line_num = 0
for line in sys.stdin.readlines():
    if line_num==0:
        line_num+=1
        continue
        
    line = line.replace('\n', '')
    evens = ''.join([line[i] for i in range(0,len(line),2)])
    odds = ''.join([line[i] for i in range(1,len(line),2)])
    print('%s %s' %(evens, odds))