# 练习1:
#   写一个函数mysum,  此函数带有两个参数x, y.
#     此函数功能是打印出两个参数x,y的和, 即 x + y

def mysum(x, y):
    print(x + y)


mysum(2, 4)


# 练习2:
#   写一个函数print_even, 传入一个数参n代表终止整数(不包含n)
#   打印:
#      2 4 6 ... n之间所有偶数:
#   函数定义格式如下:
#     def print_even(n):
#         .... <<<--- 此处自己完成
#     # 测试调用:
#     print_even(9)
#     2
#     4
#     6
#     8

def print_even(n):
    for i in range(1, n):  # 也可以加步长
        if i % 2 == 0:
            print(i)


print_even(10)


# 练习:
#   1. 写一个函数mymax, 返回两个数的最大值
#    如:
#       def mymax2(a, b):
#           ...
#       print(mymax(100, 200))  # 200
#       print(mymax("ACD", "ABCD"))  # ACD

def mymax(a, b):
    if a > b:
        max_num = a
    else:
        max_num = b
    return max_num


print(mymax(3, 10))


# 2. 写一个函数input_number() 此函数用于读取用户输入的多个整数(用户输入负数时结束输入)
# 将用户输入的数形成列表返回给调用者
#     def input_number():
#         ... # 此处自己完成

#     L = input_number()
#     print("您输入的最大数是:", max(L))
#     print("您输入的这些数的和是:", sum(L))

def input_number():
    L = []
    while True:
        i = int(input('enter a num:'))
        if i < 0:
            break
        L.append(i)
    return L


l = input_number()
print(sum(l))
print(max(l))
