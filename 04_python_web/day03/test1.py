from socket import *
import os,sys
from signal import *
import time

FILE_PATH = '/Users/roger/Documents/'

class FtpServer(object):
    def __init__(self,conn):
        self.conn = conn

    def do_list(self):
        filelist = os.listdir(FILE_PATH)
        if not filelist or filelist == None:
            self.conn.send(b'fail')
        self.conn.send(b'ok')
        time.sleep(0.1)
        for filename in filelist:
            # print(filename)
            # print(os.path.isfile(FILE_PATH + filename))
            if filename[0] != '.' and os.path.isfile(FILE_PATH + filename):
                print(filename)
                self.conn.send(filename.encode())
                time.sleep(0.1)
        self.conn.send(b'##')
        print('filelist already send...')

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH + filename,'rb')
        except Exception as e:
            print(e)
            self.conn.send(b'fail')
        self.conn.send(b'ok')
        time.sleep(0.1)
        for line in fd:
            self.conn.send(line)
        fd.close()
        time.sleep(0.1)
        self.conn.send(b'##')
        print('file send succesed...')
        return


    def do_put(self,filename):
        try:
            fd = open(FILE_PATH + filename, 'w')
        except:
            self.conn.send(b'fail')
        self.conn.send(b'ok')
        while True:
            data = self.conn.recv(1024).decode()
            if data == '##':
                break
            fd.write(data)
        fd.close()
        print('file upload sucess...')
        return



def main():
    if len(sys.argv) != 3:
        print('argv error...')
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    BUFFERSIZE = 1024

    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal(SIGCHLD, SIG_IGN)
    while True:
        try:
            conn,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue
        print("Connect from:", addr)

        pid = os.fork()
        if pid <  0:
            print('create pid fail...')
            continue
        elif pid == 0:
            sockfd.close()
            ftp = FtpServer(conn)
            while True:
                data = conn.recv(BUFFERSIZE).decode()
                if data[:4] == 'list':
                    ftp.do_list()
                elif data[:3] == 'get':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[:3] == 'put':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
                elif data[:4] == 'quit':
                    print('client quit...')
                    sys.exit(0)
        else:
            conn.close()
            continue


if __name__ == "__main__":
    main()