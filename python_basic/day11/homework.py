# 1. 编写函数 myfac(x) 计算x的阶乘x!
#    5! = 5 * 4 * 3 * 2 * 1

#   print(myfac(5))  # 120

def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x - 1)

print(myfac(10))


# 2. 写程序算出1~20的阶乘的和
#   1! + 2! + 3! + .... + 19! + 20!
#   思考:
#     能否用函数式编程中的高阶函数实现?

print(sum(map(myfac,range(1,21))))

# 3. 已知有列表:
#    L = [[3,5,8], 10, [[13, 14], 15], 18]
#   1) 写一个函数 print_list(lst) 打印出列表中所有数字
#     print_list(L)
#   2) 写一个函数sum_list(lst) 返回列表中所有数字的和
#     print(sum_list(L))  # 86
#   注:
#     type(x) 可以返回一个变量的类型
#     如:
#        >>> type(20) is int  # True
#        >>> type([1,2,3]) is list  # True

def print_list(lst):
    for i in lst:
        if type(i) is list:
            print_list(i)
        else:
            print(i)


def sumlist(lst):
    s = 0
    for i in lst:
        if type(i) is list:
            s += sumlist(i)
        else:
            s += i
    return s # TODO roger test


print_list([[3,5,8], 10, [[13, 14], 15], 18])
print(sumlist([[3,5,8], 10, [[13, 14], 15], 18]))


