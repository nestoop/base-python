#!/usr/bin/python
import socket


if __name__ == "__main__":

    HOST = "127.0.0.1"
    PORT = 9090
    serverSokcet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSokcet.bind((HOST, PORT))
    serverSokcet.listen(1)
    while 1:
        connect, address = serverSokcet.accept()

        print("connect by:", address)
        while 1:
            data = connect.recv(1024)

    connect.close





