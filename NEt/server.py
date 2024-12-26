import socket
from datetime import datetime
import threading

def time_server(host='127.0.0.1', port=65432):
    """Function to start the time server"""
    def handle_client(client_socket, client_address):
        print(f"Connection from {client_address}")
        try:
            request = client_socket.recv(1024).decode('utf-8')
            print(f"Request received: {request}")
            if request == 'GET_TIME':
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"Sending current time to {client_address}: {current_time}")
                client_socket.sendall(current_time.encode('utf-8'))
            else:
                client_socket.sendall(b"INVALID_REQUEST")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            client_socket.sendall(b"ERROR")
        finally:
            client_socket.close()
            print(f"Connection with {client_address} closed.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((host, port))
            server_socket.listen(5)
            print(f"Server is running on {host}:{port}")
            while True:
                client_socket, client_address = server_socket.accept()
                threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    print("Starting server...")
    time_server()
