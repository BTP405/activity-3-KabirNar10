import socket
import pickle
import os

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Localhost
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 connections

    print('Server listening on port', port)

    while True:
        client_socket, addr = server_socket.accept()
        print('Got a connection from', addr)

        # Make sure the 'received_files' directory exists
        received_dir = 'received_files'
        if not os.path.exists(received_dir):
            os.makedirs(received_dir)  # Create the directory if it does not exist

        received_data = client_socket.recv(1024)  # Adjust buffer size if necessary
        while received_data:
            try:
                # Unpickle the file data
                file_data = pickle.loads(received_data)
                # Save the file
                file_path = os.path.join(received_dir, file_data['filename'])
                with open(file_path, 'wb') as file:
                    file.write(file_data['file'])
                print(f"File {file_data['filename']} has been received and saved.")
                break  # Exit the loop once the file is saved
            except Exception as e:
                print('An error occurred:', e)
                break  # Exit the loop in case of error
            finally:
                received_data = client_socket.recv(1024)

        client_socket.close()

if __name__ == '__main__':
    main()
