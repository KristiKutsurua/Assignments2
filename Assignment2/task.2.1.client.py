import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
print('Connecting to', server_address)
client_socket.connect(server_address)

try:
    message = client_socket.recv(1024)
    print('Received:', message.decode())

finally:
    client_socket.close()
