# 练习：
#   输入一个数，打印指定宽度的正方形:
#   如:
#     请输入：5
#   打印正方形如下:
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   如:
#     请输入：3
#   打印正方形如下:
#   1 2 3
#   1 2 3
#   1 2 3

n = int(input("请输入："))

i = 0
while i < n:
    # print('===========')
    j = 1
    while j <= n:
        print(j, end=' ')
        j += 1
    print()  # 换行
    i += 1