import socket

HOST = "192.168.0.191"  # The server's hostname or IP address
PORT_NUMBER = 1234  # The port used by the server

# Initialize a client socket with the following parameters:
# AF_INET: specifying to use an IPv4 address
# SOCK_STREAM: spacifying to use a stream socket, e.g. TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Use the host and port (defined above) to bind the client socket to the server
client_socket.connect((HOST, PORT_NUMBER))

print(f"\nClient connected to {HOST}:{PORT_NUMBER}\n")

# Allow the user to input a message to send to the server:
message = input("Enter message to send to server: ")

# Send the message to the server, using encode() for utf-8 encoding
client_socket.sendall(message.encode())

# Wait to receive a response from the server
data = client_socket.recv(1024)

print("\nReceived the response from the server:\n\n", data.decode())

# Close the connection
client_socket.close()