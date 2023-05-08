import socket
import ssl

# Define the server host and port
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# Load the client certificate
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='server.crt')
context.load_cert_chain('server.crt', 'server.key')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
ssl_sock = context.wrap_socket(sock, server_hostname=SERVER_HOST)

# Connect to the server
ssl_sock.connect((SERVER_HOST, SERVER_PORT))

# Send data to the server
ssl_sock.sendall(b'Hello, server!')

# Receive data from the server
data = ssl_sock.recv(1024)
print(data.decode())

# Close the connection
ssl_sock.close()
