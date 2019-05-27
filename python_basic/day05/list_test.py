#循环输入字符串，空行结束，.号打印
l = []

while True:
    s = input("str:")
    l += [s]
    if s == "":
        break
print(l)
