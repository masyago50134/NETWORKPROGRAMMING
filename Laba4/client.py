import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    message = "Hello, server!"
    client.sendall(message.encode())

    data = client.recv(1024)

print("Received from server:", data.decode())
