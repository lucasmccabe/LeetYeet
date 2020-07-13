#https://www.hackerrank.com/challenges/30-interfaces

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor_sum = 0
        for i in range(1, int(n**0.5 + 1)):
            if n % i == 0:
                divisor_sum += i
                if i**2 != n:
                    divisor_sum += n/i
        return int(divisor_sum)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)