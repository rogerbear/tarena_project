a = 100000
print(id(a))


def fun(b):
    a = 100000
    print(id(a))


fun(2)


def mysum(n):
    L = []
    for i in range(1, n + 1):
        L.append(i)
    return sum(L)


print(mysum(100))


def mysum2(*args):
    s = 0
    if len(args) == 1:
        for i in range(args[0]):
            s += i
        return s
    elif len(args) == 2:
        for i in range(args[0], args[1]):
            s += i
        return s
    elif len(args) == 3:
        for i in range(args[0], args[1], args[2]):
            s += i
        return s


print(mysum2(5))
print(mysum2(4, 6))
print(mysum2(5, 10, 2))
