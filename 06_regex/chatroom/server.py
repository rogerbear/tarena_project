#聊天室服务器
from socket import * 
import sys 
import os
import signal

def do_login(s,user,name,addr):
    for i in user:
        if i == name or name == '管理员':
            s.sendto(b'FAIL',addr)
            return
    s.sendto(b'OK',addr)
    msg = "\n欢迎　%s　进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr
    return

def do_chat(s,user,tmp):
    msg = '\n%-4s: %s'%(tmp[1],tmp[2])
    for i in user:
        if i != tmp[1]:
            s.sendto(msg.encode(),user[i])
    return

def do_quit(s,user,name):
    del user[name]
    msg = '\n' + name + '离开了聊天室'
    for i in user:
        s.sendto(msg.encode(),user[i])
    return

#接收处理
def do_child(s):
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msg = msg.decode()
        tmp = msg.split(' ')
        #L name
        if tmp[0] == 'L':
            do_login(s,user,tmp[1],addr)
        #C name text
        elif tmp[0] == 'C':
            do_chat(s,user,tmp)
        #Q name
        elif tmp[0] == 'Q':
            do_quit(s,user,tmp[1])

#发送系统消息
def do_parent(s,addr):
    name = 'C 管理员 '
    while True:
        msg = input("管理员消息：")
        msg = name + msg 
        s.sendto(msg.encode(),addr)
    s.close()
    sys.exit(0)

def main():
    if len(sys.argv) != 3:
        print("argv error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    #创建数据报套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #创建进程
    pid = os.fork()
    if pid < 0:
        print("create process failed")
        return
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s,ADDR)

if __name__ == "__main__":
    main()