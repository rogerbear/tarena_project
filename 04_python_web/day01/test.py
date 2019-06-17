import socket

s = socket.gethostname()

print(s)

print(socket.gethostbyname('localhost'))

print(socket.inet_aton('192.168.1.1'))

print(socket.inet_ntoa(b'\xc0\xa8\x01\x01'))

print(socket.getservbyname('http'))
print(socket.getservbyname('https'))
print(socket.getservbyname('ssh'))
print(socket.getservbyname('ftp'))
print(socket.getservbyname('imap'))