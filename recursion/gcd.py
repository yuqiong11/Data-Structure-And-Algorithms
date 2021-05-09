# input: two non-negative integer, output: the greatest common divisor
# example: given 6, 27, output 3
# euclid's division algorithm

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print(gcd(27, 0))
print(gcd(0, 27))
print(gcd(6, 27))
print(gcd(85, 408))
