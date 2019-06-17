
#% 占位符
#类型码（d,s,f等）

#左对齐
print("%-10d" % 123)

#+显示正负号
print("%+10d" % 123)

#0补零
print("%010d" % 123)

#宽度
print("%10d" % 123)

#宽度.精度，小数点后保留n位
print("%.3f" % 123.567657657567)

print("%9.4f" % 123.6756745697)


#三行文字，以20个字符的宽度右对齐输出
print("%20s" % 'hello world')
print("%20s" % 'sfdfg')
print("%20s" % 'd')

#拿到最长字符串为宽度，用多空格填充字符串
#方法一
line1 = input('line1:')
line2 = input('line2:')
line3 = input('line3:')

ml = max(len(line1),len(line2),len(line3))
print('最长字符串长度为：',ml)
#print(' ' * (ml - len(line1)) + line1)
#print(' ' * (ml - len(line2)) + line2)
#print(' ' * (ml - len(line3)) + line3)


# 方法二
# fmt = '%' + str(ml) + 's'
#上句可写成
fmt = '%%%ds' % ml
print('格式化字符串是：',fmt)
print(fmt % line1)
print(fmt % line2)
print(fmt % line3)