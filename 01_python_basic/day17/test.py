# 　　自己写一个Student类,此类的对象有属性name, age, score, 用来保存学生的姓名，年龄，成绩
# 　　　1) 写一个函数 input_student读入n个学生的信息，用对象来存储这些信息（不用字典), 并返回对象的列表
# 2) 写一个函数output_student 打印这些学生信息(格式不限)
# 示意:
# class Student:
#    pass
# 　　　　def input_student():
#     ...　　# 获取学生信息，形成列表返回
# def output_student(lst):
#     # 打印学生信息
# def main():
#     L = input_student()
#     output_student(L)
# main()

class Student:
    pass


def input_student():
    L = []
    while True:
        n = input('请输入学生名字:')
        if n == '':
            break
        a = int(input('请输入学生年龄:'))
        sc = int(input('请输入学生成绩:'))
        s = Student()
        s.name = n
        s.age = a
        s.score = sc
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