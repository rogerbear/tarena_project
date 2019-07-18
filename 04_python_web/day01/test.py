from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

socketfd = socket(AF_INET,SOCK_STREAM)

socketfd.bind(ADDR)

socketfd.listen(5)

while True:
    print('waiting for conn...')
    conn,addr = socketfd.accept()
    print('client addr is', addr)
    while True:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print('recv data is :',data.decode())
        n = conn.send(b"recv your msg...\n")
        print('total bytes is ',n)

    conn.close()

socketfd.close()


