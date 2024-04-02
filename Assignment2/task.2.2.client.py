import socket

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode("utf-8"))

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print("Connected to server")

send_thread = threading.Thread(target=send_message)
send_thread.start()

while True:
    try:
        message = client_socket.recv(1024).decode("utf-8")
        print(message)
    except ConnectionResetError:
        print("Connection to server closed")
        break
