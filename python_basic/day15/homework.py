#  1. 用生成器函数生成斐波那契数列的前n个数:
#     1 1 2 3 5 8 13 ....
#      def fibonacci(n):
#           ...
#           yield ..
#       1) 输出前 20 个数
#       2) 求前 30 个数的和

def fibonacci(n):
    count = 0
    if count >= n:
        return
    yield 1
    count += 1

    if count >= n:
        return
    yield 1
    a = 1
    b = 1
    for i in range(2, n):
        a, b = b, a + b
        yield b


for i in fibonacci(3):
    print(i)

print(sum(fibonacci(30)))


#  2. 写程序打印杨辉三角(只打印6层)
#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1
#    1 5 10 10 5 1

def get_next_line(lst):
    next_line = [1]
    for i in range(len(lst) - 1):
        next_line.append(lst[i] + lst[i + 1])
    next_line.append(1)
    return next_line

def yh_list(n):
    L = [1]
    yhlist = []
    for i in range(n):
        yhlist.append(L)
        L = get_next_line(L)
    return yhlist

for x in yh_list(6):
    print(x)

