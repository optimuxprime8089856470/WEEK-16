import socket
import threading
def handle_client(client_socket):
    while True:
        data=client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        message=data
        if message.lower()== "exit":
            print("client requested to exit")
            break
        print(f"received messagge: {message}")
        
        
        response=(f"server received your message : {message}").encode("utf-8")
        client_socket.sendall(response)
    client_socket.close()


def main():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host='127.0.0.1'
    port=12345

    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"server listening on {host}:{ port}")

    while True:
        client_socket, addr= server_socket.accept()
        print(f"connection accepted from {addr}")
        client_handler= threading.Thread(target=handle_client, args=(client_socket,)) 
        client_handler.start()
if __name__ == "__main__":
    main()

