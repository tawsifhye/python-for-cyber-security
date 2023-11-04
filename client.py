import socket

host = '127.0.0.1'
port = 9010

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect
s.connect(((host, port)))

#client receiving data
while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input('Enter a msg  ')
    s.sendall(str.encode(data))

s.close()