# 2. 输入一个整数（代表树干的高度)
#     打印如下一棵圣诞树
#   输入:2
#     *
#    ***
#     *
#     *
#   输入:3
#     *
#    ***
#   *****
#     *
#     *
#     *

h = int(input('tree high:'))

# 打印树冠
for i in range(1, h + 1):
    stars = '*' * (2 * i - 1)
    blanks = ' ' * (h - i)#print(starts.center(2 * n - 1))
    print(blanks + stars)#print(starts.center(2 * n - 1))

for j in range(h):
    print(' ' * (h - 1) + '*')
