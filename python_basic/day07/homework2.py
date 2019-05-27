# 1. 算出 100 ~ 999 以内的水仙花数(Narcissistic Number)
#    水仙花数是指百位的3次方 加上 十位的3次方 加上个位的3次方等于原数的数字
#    例如:
#       153 等于 1**3 + 5**3 + 3**3

for x in range(100, 1000):
    ge = x % 10
    shi = x % 100 // 10
    bai = x // 100
    if x == ge ** 3 + shi ** 3 + bai ** 3:
        print(x)

# method 2
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            x = bai * 100 + shi * 10 + ge
            if x == ge ** 3 + shi ** 3 + bai ** 3:
                print(x)
