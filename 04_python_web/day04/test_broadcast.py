from socket import *

HOST = '127.0.0.1'
PORT = 8888

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind((HOST,PORT))

