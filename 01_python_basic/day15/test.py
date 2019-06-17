L = [1, 2, 3, 4, 5]
it = iter(L)

# for i in L:
#     print(i)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 已知有一个集合:
#     s = {"工商银行", "建设银行", "中国银行", "农业银行"}
#     1. 用for 语句遍历集合中的元素并打印
#     2. 将上面的for 语句改写为while语句实现上面同样的功能
#        提示: 用iter和next 函数实现

s = {"工商银行", "建设银行", "中国银行", "农业银行"}
for i in s:
    print(i)

it_2 = iter(s)
while True:
    try:
        print(next(it_2))
    except StopIteration:
        break


def my_interger(n):
    i = 1
    while i < n:
        yield i
        i += 1


for x in my_interger(5):
    print(x)


#  写入一个生成器函数, myodd(start, stop) 用于生成start开始到stop结束(不包含stop)的所有奇数
#   L = [x for x in myodd(1, 10)]
#   print(L)  # [1,3,5,7,9]
#   for x in myodd(10, 20):
#       print(x)  # 11, 13, 15, 17, 19

def myodd(start, stop):
    for i in range(start, stop):
        if i % 2:
            yield i

L = [x for x in myodd(1, 10)]
print(L)  # [1,3,5,7,9]
for x in myodd(10, 20):
    print(x)  # 11, 13, 15, 17, 19

def enter_pro():
    l = []
    while True:
        s = input('请输入：')
        if s == '':
            break
        l.append(s)
    for i,j in enumerate(l,1):
        print('第',i,'行:',j )

enter_pro()

