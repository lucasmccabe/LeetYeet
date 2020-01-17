#https://www.hackerrank.com/challenges/acm-icpc-team/

import math
import os
import random
import re
import sys


def acmTeam(topic, topic_count):
    result = [0, 0]
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            topics_covered = str(int(topic[i])+int(topic[j]))
            topics_covered_count = topic_count - topics_covered.count('0')
            if len(topics_covered)<topic_count:
                topics_covered_count-=1

            if topics_covered_count>result[0]:
                result[0]=topics_covered_count
                result[1]=1
            elif topics_covered_count==result[0]:
                result[1]+=1
            else:
                continue
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
