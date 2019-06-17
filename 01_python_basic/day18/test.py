# 练习：
# 1.
# 定义一个类Huamn(人类)
# 有三个属性:
# 姓名: name
# 年龄: age
# 家庭住址: address(可以省略没有)
# 有如下方法：
# show_info(self)
# 用来显示人的信息
# update_age(self)
# 方法用来让这个人的年龄增加一岁
#
#
# def input_human():
#     输入下此人的信息，姓名为空结束
#
#
# def main():
#     docs = input_human()
#     for h in docs:
#         h.show_info()  # 列出所有人的信息
#     for h in docs:
#         h.update_age()  # 让所有人都长一岁
#     for h in docs:
#         h.show_info()  # 再次列表所有人的信息
#
#
# main()  # 调用主函数运行

# 修改之前的Human类 让此类能够记录此类生成的对象的个数，
# 用创建一个类方法get_human_count 来获取'人对象'的个数

class Human:
    gh_count = 0
    def __init__(self, name, age, address):
        self.__class__.gh_count += 1
        self.name = name
        self.age = age
        self.address = address

    def __del__(self):
        self.__class__.gh_count -= 1

    @classmethod
    def get_human_count(cls):
        return cls.gh_count

    def show_info(self):
        print(self.name, end='')
        print(self.age, end='')
        print(self.address)

    def update_age(self):
        self.age += 1


def input_human():
    L = []
    while True:
        n = input('enter name:')
        if n == '':
            break
        a = int(input('enter age:'))
        ad = input('enter address:')
        h = Human(n, a, ad)
        L.append(h)
    return L


def main():
    docs = input_human()
    print(Human.get_human_count())
    docs += input_human()
    print(Human.get_human_count())


main()

