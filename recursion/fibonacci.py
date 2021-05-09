# fibonacci sequence 0,1,1,2,3,5,8,13,...
# input: the index of a number, output: the number

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(4))

# print the first 10 numbers
for i in range(10):
    print(fibonacci(i), end=' ')