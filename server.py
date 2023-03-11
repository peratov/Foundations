import socket

# # 1) Define IP address and PORT
#
# 127.0.0.1 is the default IP address of the computer you are currently using.
# It's the computer that the server is running on.
# This is also often referred to as "localhost"
#
# You can think of the PORT as something like a channel on a walky-talky.
# If you have multiple servers running on the same computer 
# you can use the port to direct the incoming requests to the 
# right place.
# The port number could be anything. It can be 1234, 8080, 3000, etc.
# The important part is that the client knows both the IP and the port.
#
# A common way to write IP address and PORT on the client-side is like this:
# 127.0.0.1:1234
# This is also how you can access the server from a web browser.
#
SERVER_HOST = '192.168.0.191'
SERVER_PORT = 1234

# # 2) Create a socket
#
# A socket is what's used to connect computers with each other. 
# You don't need to understand the commands below in detail.
# The important part is that the socket will "listen" to incoming
# requests based on the provided SERVER_HOST IP and SERVER_PORT.
# That means that this code is waiting and checking if any other
# device has sent a request.
#
# The print statement at the bottom is just to help visualize
# what is happening.
#
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f'🚀 Started server at: {SERVER_HOST}:{SERVER_PORT}')

# # 3) Keep listening for incoming requests
#
# Normally you run a Python program, it executes and then stops immediately.
# All of this usually happens within a few milliseconds. 
# However, this doesn't make much sense for a server. It's very unlikely
# that we start the server and within the same millisecond a client
# request comes in. 
# So instead, we need to make sure the Python code keeps running
# forever until an actual request has come in. 
# That's what the infinite loop `while True:` is for. 
#
while True:    
  print('👂 Start listening for incoming requests ...')

  # Stop the loop here and wait until a request has come in:
  client_connection, client_address = server_socket.accept()

  # The code continues running as soon as a request has come in.
  # Format the incoming request to turn it into something readable:
  request = client_connection.recv(1024).decode()

  # Print the results in the console for better visability:
  print('💬 A request has come in:')
  print(request)

  # Create and return an HTTP response:
  response = 'HTTP/1.0 200 OK\n\nHello World'
  client_connection.sendall(response.encode())
  client_connection.close()

# Close socket
server_socket.close()

# # 4) Share your server on a local network
#
# To allow others to access the server from within the local network,
# instead of using 127.0.0.1 as the IP address, you need to use
# the IP address on the network.
# This IP address is usually given to your computer by the router
# of the network (e.g., WiFi) you're connected to. 
#
# You find out your computer's network IP address with the following
# commands:
#
# Linux: hostname --ip-address
# macOS: ipconfig getifaddr en0
# Windows Powershell: ipconfig -all 
#
#(find the IP address that looks like 192.168.[...])
#