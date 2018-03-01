#!/usr/bin/python

import socket

HOST = "127.0.0.1"
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))

while 1:
    try:

        cmd = input("Please must input:")

        socket.sendall(cmd)

        data = socket.recv(1024)

        print("revivce data:", data)


    except TypeError as typeerror : 
        print("error:", typeerror.__cause__)

socket.close()
