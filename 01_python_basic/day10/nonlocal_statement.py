# nonlocal_statement.py


# 此示例示意nonlocal语句的作用

v = 100


def outter():
    v = 200
    print("outter里的v=", v)

    # 在函数内创建一个函数并调用

    def inner():
        # nonlocal v  # 声明v为外部嵌套函数的作用域内的变量,会影响上层变量
        # v += 1
        v = 400  # 函数内变量，不会影响上层变量
        print("innter里的v=", v)

        def inner_in():
            nonlocal v
            v += 1
            print('inner_in:', v)

        inner_in()

    inner()  # 调用上面的函数
    print('调用inner后,outter里的v=', v)


outter()
print("全局里的v的值是:", v)
