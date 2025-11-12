import socket

HOST = '127.0.0.1'  # Server IP
PORT = 5000         # Port number

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to the server. Type 'exit' to end chat.")

while True:
    msg = input("You: ")
    client_socket.sendall(msg.encode())
    if msg.lower() == 'exit':
        break
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Server disconnected.")
        break
    print(f"Server: {data}")

client_socket.close()
