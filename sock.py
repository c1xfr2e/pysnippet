__author__ = 'zh'

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8787))
msg = 'hello, world!'
sock.send(msg)
buf = sock.recv(len(msg))
print('echo', buf)


def recv_msg(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        msg = sock.recvfrom(1024)
        yield msg


for msg in recv_msg(('', 10001)):
    print(type(msg), msg)

