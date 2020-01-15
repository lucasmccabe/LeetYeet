#https://www.hackerrank.com/challenges/30-dictionaries-and-maps

import sys

def build_phonebook(records):
    phonebook = {}
    for record in records:
        record = record.split()
        phonebook[record[0]] = record[1]
    return phonebook

if __name__ == '__main__':
    n = int(input())

    lines = [line.replace('\n', '') for line in sys.stdin.readlines()]
    records = [lines[i] for i in range(n)]

    phonebook = build_phonebook(records)

    for line in lines[n:]:
        if line not in phonebook:
            print('Not found')
        else:
            print('%s=%s' %(line, phonebook[line]))