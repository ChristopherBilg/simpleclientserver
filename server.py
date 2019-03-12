#!/usr/bin/env python2

import socket

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024


def reverse_text(text):
    return text[::-1]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print("Connection: " + str(connection))
print("Address: " + str(address))

data = connection.recv(BUFFER_SIZE)
if not data:
    exit
print("Data received: " + str(data.decode()))
connection.send(reverse_text(data).encode())

connection.close()
