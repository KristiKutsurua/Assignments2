import socket
import threading

def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received message from {addr}: {message}")
            with open("chat_log.txt", "a") as f:
                f.write(f"{addr[0]}: {message}\n")
            broadcast(message)
        except ConnectionResetError:
            break
    print(f"Connection from {addr} closed")
    client_socket.close()

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode("utf-8"))
        except:
            clients.remove(client)

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

clients = []

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
