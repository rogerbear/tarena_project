from socket import * 


HOST = ''
PORT = 9999

#使用数据报套接字
s = socket(AF_INET,SOCK_DGRAM)

#设置套接字为允许广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind((HOST,PORT))

while  True:
    try:
        message,addr = s.recvfrom(1024)
        print('get msg from',addr)
        print("广播通知:",message.decode())
        s.sendto('收到广播了'.encode(),addr)
    except Exception as e:
        print(e)
s.close()