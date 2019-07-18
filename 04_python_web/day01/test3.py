from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

connfd = socket(AF_INET, SOCK_STREAM)

connfd.connect(ADDR)
while True:
    data = input('send something... >>')
    if not data:
        break
    connfd.send(data.encode())

    data = connfd.recv(BUFFERSIZE)
    print(data.decode())

connfd.close()
