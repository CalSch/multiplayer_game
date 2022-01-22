import socket,json

HOST = input("server ip: ")
PORT = 7777


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

