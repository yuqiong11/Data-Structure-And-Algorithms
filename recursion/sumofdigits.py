# input: a number, output: the sum of digits of that number
# example1: given 12, output 3
# example2: given 101, output 2

def sumofDigits(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sumofDigits(n//10)

print(sumofDigits(12))
print(sumofDigits(101))
print(sumofDigits(5678))