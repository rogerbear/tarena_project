# 4. 输入一个正整数，打印这个数是否是素数(prime)
#   提示:
#     素数也叫质数,是只能被1和自身整数的整数
#   如：
#     请输入: 5
#   打印:
#     5 是素数

#     请输入: 6
#   打印:
#     6 不是素数

#   素数: 2 3 5 7 11 13 17 19 23 ...

n = int(input('enter a num: '))

if n < 2:
    print(n, '不是素数')
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, '不是素数')
            break
    else:
        print(n, '是素数')