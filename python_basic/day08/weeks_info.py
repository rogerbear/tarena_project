# 练习：
#   输入一个字符串代表星期几(0~6), "0"/'日'代表周日，'1'/'一' 代表周一.
#   '2'/'二' 代表周二.......... '6'/'六' 代表 周六
#   任意输入字符串，打印这个字符串是否代表星期几,如果不是以上字符打印"字典内没有相应的数据"
#     (要求将以上数据存于字典中, 键为字符串:'0123456日一二三...六'中的一个，值为星期几或周几)
#   d = {
#        '0': "星期天",
#        '日': "星期天",
#        '1': "星期一",
#        .....
#       }

d = {
    '0': "星期天",
    '1': "星期一",
    '2': "星期二",
    '3': "星期三",
    '4': "星期四",
    '5': "星期五",
    '6': "星期六",
    '日': "星期天",
    '一': "星期一",
    '二': "星期二",
    '三': "星期三",
    '四': "星期四",
    '五': "星期五",
    '六': "星期六",  # 最后一个逗号可能会出问题
}

while True:
    s = input("请输入期星的代码: ")
    if not s:  # 当用户输入空字符串时结束输入
        break
    if s in d:  # 判断s是否是d的键
        print("您输入的是: ", d[s])
    else:
        print("您的输入不正确，请输重新输入!")

