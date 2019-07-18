from socket import *

HOST = '127.0.0.1'
PORT = 8999
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

socketfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('消息>>')
    if not data:
        break

    socketfd.sendto(data.encode(),ADDR)
    data,addr = socketfd.recvfrom(BUFFERSIZE)
    print('收到服务器返回的：',data.decode())

socketfd.close()