import socket
import pickle
import os

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    try:
        client_socket.connect((host, port))
        file_path = input("Enter the path of the file to transfer: ")
        filename = os.path.basename(file_path)

        # Ensure the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            return

        # Read the file and pickle the file data
        with open(file_path, 'rb') as file:
            file_data = {'filename': filename, 'file': file.read()}
            pickled_file_data = pickle.dumps(file_data)
            client_socket.send(pickled_file_data)
            print("File has been sent successfully.")

    except Exception as e:
        print('An error occurred:', e)
    finally:
        client_socket.close()

if __name__ == '__main__':
    main()
