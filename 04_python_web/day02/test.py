from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 8999
ADDR = (HOST,PORT)
BUFFERSIZE = 5

socketfd = socket(AF_INET,SOCK_DGRAM)

socketfd.bind(ADDR)

while True:
    data,addr = socketfd.recvfrom(BUFFERSIZE)
    print('从',addr,'收到了：',data.decode())
    socketfd.sendto(('在%s接收到你的消息' % ctime()).encode(), addr)

socketfd.close()