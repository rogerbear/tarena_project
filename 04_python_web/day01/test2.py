from socket import *

HOST = '127.0.0.1'
PORT = 8999
ADDR = (HOST,PORT)

connfd = socket(AF_INET,SOCK_STREAM)

connfd.connect(ADDR)

while True:
    data = input('send something >>')
    if not data:
        break
    connfd.send(data.encode())

    data = connfd.recv(1024)
    print('recv data: ',data.decode())

connfd.close()