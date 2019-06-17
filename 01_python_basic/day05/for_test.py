# 计算空格数，不能用S.count方法
n = input("enter a str: ")
count = 0
for i in n:
    if i == ' ':
        count += 1
print(count)

# 用while语句实现
n = input("enter a str: ")
lenth = len(n)
count = 0
i = 0
while i < lenth:
    s = n[i]
    if s == ' ':
        count += 1
    i += 1
print(count)
