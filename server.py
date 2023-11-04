import socket

host = '127.0.0.1'
port = 9010


#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection setup
s.bind((host, port))
s.listen()
client, addr = s.accept()

print(f'Connection receive from {addr}')

while True:
    data = input('Enter a msg  ')
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)
client.close()