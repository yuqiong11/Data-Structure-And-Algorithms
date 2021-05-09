# input: base and exponent, output: base^exponent

def powerofNum(base, exp):
    if exp == 0:
        return 1
    else:
        return base * powerofNum(base, exp - 1)


print(powerofNum(3, 4))
