# 集合练习:
#   经理有: 曹操，刘备，周瑜
#   技术员有: 曹操，周瑜，张飞，赵云
#   用集合求:
#     1. 即是经理也是技术员的有谁?
#     2. 是经理，但不是技术员的有谁？
#     3. 是技术人员，但不是经理的都有谁?
#     4. 张飞是经理吗？
#     5. 身兼一职的人都有谁?
#     6. 经理和技术员共有几个人?
#     

manager = {'曹操', '刘备', '周瑜'}
tech = {'曹操', '周瑜', '张飞', '赵云'}

m_t = manager & tech
print(m_t)

m_n_t = manager - tech
print(m_n_t)

t_n_m = tech - manager
print(t_n_m)

print('张飞' in manager)

one_m_or_t = manager ^ tech
print(one_m_or_t)

count = manager | tech
print(len(count))

# manager = {'曹操', '刘备', '周瑜'}
# tech = {'曹操', '周瑜', '张飞', '赵云'}
# print("即是经理也是技术员的有:", manager & tech)
#
# print("是经理，但不是技术员的有:", manager - tech)
# print("是技术人员，但不是经理的都有:", tech - manager)
# print("张飞", "是" if "张飞" in manager else "不是", "经理")
# print("身兼一职的人都有谁", manager ^ tech)
# print("经理和技术员共有%d个人" % len(manager | tech))
