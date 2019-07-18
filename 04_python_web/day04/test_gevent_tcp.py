import gevent
from gevent import monkey

monkey.patch_all()
from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
s = socket()
s.bind(ADDR)
s.listen(20)


def handler(c, addr):
    print('Connect from ', addr)
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("Recv msg ", data)
        c.send(b'recv your msg')
    c.close()




while True:
    c, addr = s.accept()
    gevent.spawn(handler, c, addr)

s.close()
