# 1. 已知有五位朋友在一起
#     第五位朋友比第四个人大2岁
#     第四位朋友比第三个人大2岁
#     第三位朋友比第二个人大2岁
#     第二位朋友比第一个人大2岁
#     第一个人说他今年10岁,
#     编写程序算出第5个人几岁

x = 10
for _ in range(4):
    x = x + 2
print(x)
