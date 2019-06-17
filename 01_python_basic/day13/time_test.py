import time

print('%02d:%02d:%02d' % (time.localtime()[3], time.gmtime()[4], time.gmtime()[5]))


t = (1986,8,9,0,0,0,0,0,0)
bir = time.mktime(t)
print(time.localtime(bir)[6])