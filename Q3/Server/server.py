# server.py
import socket
import threading
import pickle

# List to keep track of connected clients
clients = []
lock = threading.Lock()

def broadcast(message):
    with lock:
        for client in clients:
            client.send(message)

def handle_client(conn):
    while True:
        try:
            # Receiving and unpickling the message
            message = conn.recv(1024)
            if message:
                print(f"Received: {pickle.loads(message)} from {conn}")
                broadcast(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            with lock:
                clients.remove(conn)
            conn.close()
            break

def main():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print("Server is listening...")

    while True:
        conn, addr = s.accept()
        with lock:
            clients.append(conn)
        print(f"Connected to {addr}")
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

if __name__ == "__main__":
    main()
