class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def input_student():
    L = []
    while True:
        n = input('请输入学生名字:')
        if n == '':
            break
        a = int(input('请输入学生年龄:'))
        sc = int(input('请输入学生成绩:'))
        s = Student(n, a, sc)
        L.append(s)
    return L


def output_student(lst):
    for s in lst:
        print('姓名：', s.name,
              '年龄：', s.age,
              '分数：', s.score
              )


def main():
    L = input_student()
    output_student(L)


main()
