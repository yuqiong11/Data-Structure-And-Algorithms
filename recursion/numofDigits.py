# input: a number, output: number of digits
# example1: given 10, output 2
# example2: given 123, output 3

def numofDigits(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + numofDigits(n // 10)

print(numofDigits(0))
print(numofDigits(34))
print(numofDigits(999))
print(numofDigits(6666))