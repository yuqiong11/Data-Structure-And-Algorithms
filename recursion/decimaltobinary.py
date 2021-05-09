# input: a decimal number, output：binary number
# example: given 5, output 101

# 5/2=2...1
# 2/2=1...0
# 1/2=0...1  quotient is 0, stop!

# 5=2*2+1  -> 101=10*10+1
# 2=2*1+0  -> 10 =10*1+0
# 1=2*0+1  -> 1  =10*0+1

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(n // 2)


print(decimalToBinary(6))
print(decimalToBinary(15))


# def decimalToBinary1(n):
#     if n>=1:
#         decimalToBinary1(n // 2)
#         print(n % 2, end='')
#
# decimalToBinary1(11)
