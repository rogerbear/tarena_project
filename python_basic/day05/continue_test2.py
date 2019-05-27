# 求1-100之间不能被5，7，11整除的数的和

s = 0
for i in range(1, 101):
    if (i % 5 == 0 or i % 7 == 0 or i % 11 == 0):
        continue
    s += i
else:
    print(s)