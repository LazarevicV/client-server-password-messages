import socket 

def handle_client(server_socket, password):

    correct_password = False
    while True:

        if not correct_password:
            client_socket, client_address = server_socket.accept()
            print('New client is connected!')
            client_socket.send('Welcome, client!'.encode())


            recieved_password = client_socket.recv(1024).decode()

            if recieved_password != password:
                client_socket.send('fail'.encode())
                print('Client did not enter a correct message!')
                client_socket.close()
            else:
                client_socket.send('correct'.encode())
                print('Client entered a correct password!')
                correct_password = True
            
        else:
            recieved_message = client_socket.recv(1024).decode()

            print(f'Client sent a message: {recieved_message}')

            if (recieved_message == 'kraj'):
                print('Client terminated connection')
                client_socket.close()
                correct_password = False

            else:
                client_socket.send(recieved_message.upper().encode())
                print(f'Response to clients message: {recieved_message.upper()}')

def start_server():

    address = ('127.0.0.1', 2023)

    password = "abc"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)
    print('Server slusa na portu 2023')

    handle_client(server_socket, password)

start_server()