import socket 

address = ('127.0.0.1', 2023)


def connect_to_server(address):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)

    return client_socket

def recieve_message(client_socket):
    message = client_socket.recv(1024).decode()
    print(f'Server sent you a message: {message}')

def enter_message(client_socket):
    while True:
        message = input('Enter a message: ')

        if message == 'kraj':
            client_socket.send(message.encode())
            print('Connection is terminated.')
            break 
        else:
            client_socket.send(message.encode())
            recieved_message = client_socket.recv(1024).decode()
            print(recieved_message)
    

def enter_password(client_socket):
    password = input('Enter password: ')
    client_socket.send(password.encode())
    status = client_socket.recv(1024).decode()
    if status == 'correct':
        print(f'Server accepted your password!')
        enter_message(client_socket)
        
    else:
        print(f'Your password was not accepted by the server!')


client_socket = connect_to_server(address)
recieve_message(client_socket)
enter_password(client_socket)
