#https://www.hackerrank.com/challenges/30-queues-stacks/

import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []
    
    def pushCharacter(self, ch: str):
        """
        Pushes a character onto the stack.
        """
        self.stack = [ch] + self.stack
        return None
    
    def enqueueCharacter(self, ch: str):
        """
        Enqueues a character onto the queue.
        """
        self.queue = [ch] + self.queue
        return None

    def popCharacter(self):
        """
        Removes character from stack (LIFO) and returns it.
        """
        if self.stack:
            ch = self.stack[0]
            self.stack = self.stack[1:]
            return ch
        return None

    def dequeueCharacter(self):
        """
        Removes character from queue (FIFO) and returns it.
        """
        if self.queue:
            ch = self.queue[-1]
            self.queue = self.queue[:-1]
            return ch
        return None

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    