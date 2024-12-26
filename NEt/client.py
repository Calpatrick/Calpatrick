import socket

def time_client(host='127.0.0.1', port=65432):
    """Function for the client to request time"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"Connecting to server at {host}:{port}")
            client_socket.connect((host, port))
            client_socket.sendall(b'GET_TIME')
            response = client_socket.recv(1024).decode('utf-8')
            if response == "ERROR":
                print("Server encountered an error.")
            elif response == "INVALID_REQUEST":
                print("Invalid request sent to the server.")
            else:
                print(f"Server Response: {response}")
    except socket.error as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    time_client()
