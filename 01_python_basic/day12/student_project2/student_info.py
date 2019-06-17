# student_info.py
# 2. 改写之前的学生信息管理项目源码，要求带有操作界面:
#     +------------------------------+
#     | 1) 添加学生信息                |
#     | 2) 显示所有学生的信息           |
#     | 3) 删除学生信息                |
#     | 4) 修改学生成绩                |
#     | 5) 按学生成绩高-低显示学生信息   |
#     | 6) 按学生成绩低-高显示学生信息   |
#     | 7) 按学生年龄高-低显示学生信息   |
#     | 8) 按学生年龄低-高显示学生信息   |
#     | q) 退出                       |
#     +------------------------------+
#     请选择:
#     要求，每个功能至少写一个函数与之相对应


def input_student():
    lst = []  # 创建一个空列表用于存储学生的信息(字典)
    while True:
        n = input("请输入学生姓名: ")
        if not n:
            break
        a = int(input("请输入学生年龄: "))
        s = int(input("请输入学生成绩: "))
        # 创建一个新的字典
        d = {'name': n,
             'age': a,
             'score': s
             }
        lst.append(d)  # 把字典放入列表中
    return lst


def output_studnet(lst):
    print("+-----------+--------+---------+")
    print("|   name    |  age   |  score  |")
    print("+-----------+--------+---------+")

    for d in lst:  # d绑定学生信息的字典
        info = "| %9s | %6d | %7d |" % (
            d['name'], d['age'], d['score']
        )
        print(info)

    print("+-----------+--------+---------+")


def delete_student(lst):
    s = input('请输入要删除的学生名字：')
    count = 0
    for d in lst:
        if s in d['name']:
            del lst[count]
        count += 1
    output_studnet(lst)


def modify_student(lst):
    flag = True
    count = 0
    while flag:
        s = input('请输入要修改成绩的学生名字：')
        for d in lst:
            if s == d['name']:
                sc = int(input('请输入新的成绩：'))
                lst[count]['score'] = sc
                flag = False
                break
            count += 1
        else:
            print('no this student!')
            count = 0
            continue
    output_studnet(lst)


def score_key(l):
    return l['score']


def score_sort_reverse(lst):
    lst.sort(key=lambda k: k['score'], reverse=True)
    # lst.sort(key=score_sort, reverse=True)  # 也可以直接用lst.sort(key = lambda k:k['age'])
    output_studnet(lst)


def score_sort(lst):
    # lst.sort(key=lambda k: k['score'])
    lst.sort(key=score_key)
    output_studnet(lst)


def age_sort_reverse(lst):
    lst.sort(key=lambda k: k['age'], reverse=True)
    output_studnet(lst)


def age_sort(lst):
    lst.sort(key=lambda k: k['age'])
    output_studnet(lst)


def show_menu():
    print("1) 添加学生")
    print("2) 显示学生")
    print("3) 删除学生")
    print("4) 修改成绩")
    print("5) 成绩高到低")
    print("6) 成绩低到高")
    print("7) 年龄高到低")
    print("8) 年龄低到高")
    print("q) 退出")


def main():
    docs = []  # 此列表用于存储所有学生的信息
    while True:
        # 显示菜单
        show_menu()
        # 让用户做出选择
        s = input("请选择: ")
        # 根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_studnet(docs)
        elif s == '3':  # 删除学生信息
            delete_student(docs)
        elif s == '4':  # 修改学生成绩
            modify_student(docs)
        elif s == '5':  # 成绩高到低
            score_sort_reverse(docs)
        elif s == '6':  # 成绩低到高
            score_sort(docs)
        elif s == '7':  # 年龄高到低
            age_sort_reverse(docs)
        elif s == '8':  # 年龄低到高
            age_sort(docs)


main()
