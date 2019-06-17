import math

# 求面积
r = 10
print(math.pi * r ** 2)

# 求半径
s = 100
print(math.sqrt(s / math.pi))


def fun(n):
    Sn = 0
    for i in range(n + 1):
        Sn += 1 / math.factorial(i)
    print(Sn)


fun(20)


def fun2(x, n):
    s = 0
    for i in range(n + 1):
        s += math.pow(x, i) / math.factorial(i)
    return s


print(fun2(3.1,10))
print(fun2(1,10))
