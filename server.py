import socket

HOST = '127.0.0.1'  # Localhost
PORT = 5000         # Port number

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started on {HOST}:{PORT}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Client disconnected.")
        break
    print(f"Client: {data}")
    msg = input("You: ")
    conn.sendall(msg.encode())
    if msg.lower() == 'exit':
        break

conn.close()
server_socket.close()
