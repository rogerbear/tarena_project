# 3.用while 循环生成如下字符串:
#    1. 生成'ABCDEFG...... XYZ' 并打印
#    2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
#    提示:
#      用chr和ord函数

print(chr(97))
print(chr(122))
print(chr(65))
print(chr(90))

#    1. 生成'ABCDEFG...... XYZ' 并打印
# AZ = ""
i = ord('A')
while i <= ord("Z"):
    print(chr(i), end="")
    i += 1
else:
    print()

#    2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
i = ord('A')
j = ord('a')
while i <= ord('Z'):
    print(chr(i) + chr(j), end='')
    i += 1
    j += 1
