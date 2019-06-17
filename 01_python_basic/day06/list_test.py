# 练习：
#   写一个程序，让用户输入很多个正整数，当输入小于零的数时结束输入
#   1)  输出这些数的和
#   2)  输出这些数的最大的数和第二大的数
#   3)  删除最小的一个数
#   4)  按原来输入的顺序打印出剩余的这些数


l = []
while True:
    n = int(input('enter a num: '))
    if n < 0:
        break
    l.append(n)
print(l)
#   1)  输出这些数的和
print('sum:', sum(l))
#   2)  输出这些数的最大的数和第二大的数
l2 = l.copy()
l2.sort(reverse=True)
print('max:', l2[0])
print('max_second:', l2[1])
#   3)  删除最小的一个数
l.remove(min(l))
#   4)  按原来输入的顺序打印出剩余的这些数
for i in l:
    print(i)
