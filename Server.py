import socket
import ssl
import os

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12345

# Load the server certificate and private key
server_cert = 'server.crt'
server_key = 'server.key'

# Create an SSL context and load the server certificate and key
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

# Create a TCP/IP socket and bind it to the server address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(1)

# Wrap the socket in an SSL socket
ssl_server_socket = context.wrap_socket(server_socket, server_side=True)

# Accept incoming connections and handle them
while True:
    try:
        # Wait for a client to connect
        print('Waiting for a connection...')
        client_socket, client_address = ssl_server_socket.accept()
        print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

        # Receive data from the client
        data = client_socket.recv(1024)
        print(data.decode())

        # Send a response back to the client
        response = b'Hello, client!'
        client_socket.sendall(response)
    except ssl.SSLError as e:
        print('SSL Error: {}'.format(e))
    except socket.timeout:
        print('Timeout occurred')
    except Exception as e:
        print('Exception occurred: {}'.format(e))
    finally:
        # Close the client socket
        client_socket.close()
                                       
