#输入一个数，返回绝对值，不能用abs方法

i = input("input a num:")
inp = int(i)

if inp >= 0:
    print(inp)
else:
    print(-inp)


i = input("input a num:")
inp = int(i)

out = inp if inp >= 0 else -inp
print(out)

