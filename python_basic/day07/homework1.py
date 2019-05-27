# 2. 任意输入一些大于零数，存于列表中L,当输入-1时结束输入
#   L = [1, 3, 5, 3, 7, 9, 3, 7, 6, 5]
#   1) 打印出这些数
#   2) 打印出这些数的和
#   3) 去掉列表L中重复第二次或之后出现的数，再次存到另一个列表L2中
#      L2 = [1, 3, 5, 7, 9, 6]
#      打印这些数
#   4) 打印L2列表中的数据的和
#   5) 将 L列表中，出现两次的数存到另一个列表L3中
#        L3 = [5, 7]

L = []
while True:
    n = int(input('enter a num: '))
    if n == -1:
        break
    else:
        L.append(n)
print(L)
print(sum(L))

L2 = []
for x in L:
    if x not in L2:
        L2.append(x)
print(L2)
print(sum(L2))

L3 = []
for y in L:
    if L.count(y) == 2:
        if y not in L3:
            L3.append(y)
print(L3)
