s = 'hello world haha'
l = s.split(' ')
print(l)

l2 = ['c:', 'programe files', 'python']
s2 = "\\".join(l2)
print(s2)

n = input('enter a str:')
# print(type(n))
s3 = 'hello'
l3 = n.join(s3)
print(l3)

# 列表推导式
c = [x ** 2 for x in range(10)]
print(c)

# 列表推导式2 带if判断
c2 = [x ** 3 for x in range(10) if x > 0]
print(c2)
