# client.py
import socket
import pickle
from tasks import add, multiply

def send_task(task, *args):
    task_data = pickle.dumps((task, args))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(task_data)
        data = s.recv(1024)
    return pickle.loads(data)

if __name__ == "__main__":
    # Example usage
    print("Result of addition:", send_task(add, 3, 4))
    print("Result of multiplication:", send_task(multiply, 3, 4))
