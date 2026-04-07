import socket
import threading

def main():
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host="127.0.0.1"
    port = 12345
    client_socket.connect((host, port))

    while True:
        message=input("Enter you message: ")
        if message.lower()== "exit":
            break
        client_socket.sendall(message.encode("utf-8"))
        data= client_socket.recv(1024).decode("utf-8")
        response=data
        print(f"server response: {response}")
    
if __name__ == "__main__":
    main()