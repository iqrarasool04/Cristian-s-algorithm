import socket
import time

#function to synchronize client time with server
def synchronize_time(server_address):

    #socket creation and connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    #sending request to server
    T_0 = time.time()
    client_socket.send(str(T_0).encode())

    #receiving time from server
    T_1 = float(client_socket.recv(1024).decode())

    #calculating synchronized clock time
    T_CLIENT = T_1 + (T_1 - T_0) / 2
    print(f"Synchronized Client Clock Time: {T_CLIENT}")

    #closing socket
    client_socket.close()

server_address = ('localhost', 12345)
synchronize_time(server_address)
