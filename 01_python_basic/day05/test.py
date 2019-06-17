for x in 'abc':
    for y in '123':
        print(x + y)

#    for 循环生成如下字符串:
#    1. 生成'ABCDEFG...... XYZ' 并打印
#    2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
#    提示:
#      用chr和ord函数
for x in range(ord('A'), ord('Z') + 1):
    print(chr(x), end=' ')
print()

for x in range(ord('A'), ord('A') + 26):
    print(chr(x) + chr(x + 0x20), end=' ')#0x20=32，差值
print()

# 练习：
#   用 for 循环嵌套打印如下矩形:
#     （输入一个数n(10以内) 代表矩形的宽度和高度)
#   如:
#     请输入: 5
#   打印如下：
#   1 2 3 4 5
#   2 3 4 5 6
#   3 4 5 6 7
#   4 5 6 7 8
#   5 6 7 8 9
#     请输入: 3
#   打印如下：
#   1 2 3
#   2 3 4
#   3 4 5

n = int(input('enter a num: '))
for x in range(1, n + 1):
    for y in range(x, x + n):
        print(y, end=' ')
    else:
        print()
