# coding=utf-8

import socket
import threading


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_handler(conn):
    while True:
        req = conn.recv(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode("utf8") + b'\n'
        conn.send(resp)
    print("Closed")


def fib_server(address):
    sock = socket.socket()
    sock.bind(address)
    sock.listen()

    while True:
        conn, addr = sock.accept()
        print("Connection", addr)
        threading.Thread(target=fib_handler, args=(conn,)).start()


fib_server(('', 25000))
