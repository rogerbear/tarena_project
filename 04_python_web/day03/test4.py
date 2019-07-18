from socket import *
import select
import sys

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8888))
s.listen(5)

fdmap = {s.fileno(): s}

p = select.poll()

p.register(s)

while True:
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connect from ', addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send(b'already recv msg...')
s.close()