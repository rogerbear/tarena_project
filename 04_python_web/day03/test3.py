import select
from socket import *
import sys

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1',8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    rs, ws, es = select.select(rlist, wlist, xlist)
    print('IO is comming...')
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print('connect from', addr)
            rlist.append(c)
            xlist.append(c)
        else:  # 或者写 if r is c:
            data = r.recv(1024).decode()
            if not data:
                print('client is exit...')
                rlist.remove(r)
                xlist.remove(r)
                r.close()
            else:
                wlist.append(r)
            print('recv client msg:', data)

    for w in ws:
        r.send(b'already recv your msg...')
        wlist.remove(w)

    for e in es:
        if e is s:
            s.close()
            sys.exit(0)
        else:
            e.close()
            rlist.remove(e)
            xlist.remove(e)
s.close()
