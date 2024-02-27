# client.py
import socket
import threading
import pickle

def receive_messages(s):
    while True:
        try:
            message = s.recv(1024)
            if message:
                print(pickle.loads(message))  # Print only messages received from the server.
        except Exception as e:
            print(f"An error occurred: {e}")
            s.close()
            break

def main():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    threading.Thread(target=receive_messages, args=(s,)).start()

    while True:
        message = input()  # User types a message.
        s.send(pickle.dumps(message))  # Don't print it here, it gets printed when received back from the server.

if __name__ == "__main__":
    main()
