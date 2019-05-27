def input_student():
    lst = []
    while True:
        n = input('请输入姓名：')
        if not n:
            break
        a = int(input('请输入年龄：'))
        s = int(input('请输入分数：'))
        d = {'name': n,
             'age': a,
             'score': s}
        lst.append(d)
    return lst



def output_student(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")
    for i in lst:
        print('| %9s | %6d | %7d |' %
              (i['name'],i['age'],i['score']))
    print("+-----------+--------+---------+")

L = input_student()
print(L)
output_student(L)
