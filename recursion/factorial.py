# factorial of an non-negative integer
# input: number, output: factorial of the number

def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(0))
print(factorial(3))