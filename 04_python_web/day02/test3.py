from socket import *
from threading import *
import os

HOST = '127.0.0.1'
PORT = 8999
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

# 4、有客户端断开则关闭响应的子进程
def handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print('接收到了：',data)
        c.send('已经收到你的消息'.encode())
    c.close()


# 1、创建套接字  绑定  监听
s = socket()
s.bind(ADDR)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(5)



# 2. 接收客户端连接请求  创建新的进程
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        print('服务器退出')
        s.close()
        os._exit(0)
    except Exception:
        continue
    print('接收到客户端连接：',c.getpeername())

    th = Thread(target=handler,args=(c,))
    th.setDaemon(True)
    th.start()




