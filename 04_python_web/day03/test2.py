from socket import *
import sys, time


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'list')

        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            while True:
                data = self.sockfd.recv(1024).decode()
                if data == '##':
                    break
                print(data)
            print('filelist all layout...')
            return
        else:
            print('file list request fail...')
            return

    def do_get(self, filename):
        self.sockfd.send(('get ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        print(data)
        if data == 'ok':
            fd = open(filename, 'w')
            while True:
                data = self.sockfd.recv(1024).decode()
                if data == '##':
                    break
                fd.write(data)
            fd.close()
            print('%s download finish...' % filename)
            return

        else:
            print('download fail...')
            return

    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except:
            print('file not exit...')
            return

        self.sockfd.send(('put ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            for line in fd:
                self.sockfd.send(line)
            fd.close()
            time.sleep(0.1)
            self.sockfd.send(b'##')
            print('send %s sucess...' % filename)
            return
        else:
            print('upload fail...')
            return

    def do_quit(self):
        self.sockfd.send(b'quit')


def main():
    if len(sys.argv) != 3:
        print('argv error')
        sys.exit(0)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024
    sockfd = socket()
    sockfd.connect(ADDR)
    ftp = FtpClient(sockfd)
    while True:
        print('****order choice****')
        print('****list****')
        print('****get****')
        print('****put****')
        print('****quit****')
        data = input('input order>>')
        if data[:4] == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)
        elif data[:4] == 'quit':
            ftp.do_quit()
            sockfd.close()
            sys.exit(0)
        else:
            print('please check your order')
            continue


if __name__ == "__main__":
    main()
