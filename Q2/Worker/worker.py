# worker.py
import socket
import pickle
from tasks import *

def execute_task(task_data):
    task, args = pickle.loads(task_data)
    return task(*args)

def main():
    host = ''
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Worker listening on port", port)
        while True:
            conn, addr = s.accept()
            with conn:
                print('Received a task from', addr)
                task_data = conn.recv(1024)
                result = execute_task(task_data)
                conn.sendall(pickle.dumps(result))

if __name__ == "__main__":
    main()
