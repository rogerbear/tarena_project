f = open('tset.bin','wb')
f.write(b'hello\xe4\xb8\xad')

s = '我是汉字'
r = f.write(s.encode('utf-8'))
print(r)
f.close()
