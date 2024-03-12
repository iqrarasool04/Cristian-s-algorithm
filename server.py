import socket
import time

#function for sending time to client
def start_server(server_address):

    #socket creation and connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Clock Server is listening...")

    while True:
        #accepting connection and receiving request from client
        client_socket, client_address = server_socket.accept()
        T_0 = float(client_socket.recv(1024).decode())

        #sending server's time to client
        T_SERVER = time.time()
        client_socket.send(str(T_SERVER).encode())

        #closing socket
        client_socket.close()

server_address = ('localhost', 12345)
start_server(server_address)
