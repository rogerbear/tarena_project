#判断输入的字符串有几个字符'e'
s= input('enter a str:')

print('e的个数是：',s.count('e'))

#判断输入包含多少个空格

print('空格个数是：',s.count(' '))

#判断输入字符串是否以？结尾
if s.endswith('?'):
    print('问号结尾')
else:
    print('不以问号结尾')
