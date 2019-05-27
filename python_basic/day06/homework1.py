# 练习：
#   1. 输入一个整数n 代表结束的数.
#   将 1 ~ n之间所有的素数计算出来并存入到列表L 中
#     1) 最后打印此列表中的全部素数
#     2) 打印这些素数的和

n = int(input('enter a num: '))
L = []
for x in range(1, n + 1):
    if x < 2:
        continue
    for i in range(2, x):
        if x % i == 0:
            print(x,'不是素数')
            break
    else:
        print(x,'是素数')
        L.append(x)
print(L)
print(sum(L))
