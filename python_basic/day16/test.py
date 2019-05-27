def fib(n):
    a = 1
    b = 1
    l = [1, 1]
    for i in range(2, n):
        a, b = b, a + b
        l.append(b)
    return l


print(fib(5))

try:
    file = open('test.txt')
    r = file.readline()
    print('test1:', r)
    file.close()
except IOError:
    print('open fail...')


# 练习:
#     将如下数据用文本编辑器sublime 写入到data.txt文件中
#     数据如下:
#       小张 13888888888
#       小李 13999999999
#       小赵 13666666666
#     写程序读取数据，打印出姓名和电话号码,格式如下：
#     　　姓名: 小张, 电话: 13888888888


def read_data():
    f = open('test.txt')
    l = []
    while True:
        data = f.readline().rstrip().split(' ')
        if data == ['']:
            f.close()
            return l
        l.append(data)


def read_phone_book(lst):
    for i in lst:
        print('姓名:', i[0], ',电话:', i[1])


read_phone_book(read_data())


# 练习：
#   1. 写一个程序，读入任意行的文字信息，当输入空行时结束输入.
#   将读入的字符串存于列表中,然后将列表里的内容写入的文件 input.txt 中
#
#   2. 写一个程序, 从input.txt中读取之前输入的数据，存入列表中．再加上行号进行打印显示
#     　显示格式如下　：
#     　　　　第1行: zzzzzzz
#         第2行: xxxxxxx

def write_data():
    try:
        L = []
        while True:
            s = input('输入的内容：')
            if s == '':
                break
            L.append(s + '\n')
        f = open('input.txt', 'w')
        f.writelines(L)
        f.close()
    except IOError:
        print('写文件失败...')

write_data()


def read_data():
    f = open('input.txt')
    L = f.readlines()
    for i in L:
        print('第一行：', i, end='')
    f.close()

read_data()