import socket

BUFFER_SIZE = 16

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client_socket.connect(("127.0.0.1", 20000))

while True:
    my_message = input("> ")
    if not my_message:
        my_message = " "
    client_socket.sendall(my_message.encode('utf-8'))

    # received_message = client_socket.recv(4096)
    # chunk = client_socket.recv(BUFFER_SIZE)
    # chunks.append(chunk)
    chunks = []
    bytes_recd = BUFFER_SIZE
    while bytes_recd >= BUFFER_SIZE:
        # print(f"1 +++ {chunk}, len {len(chunk)}")
        
        # print(f">>> chunks: {chunks}")
        # if len(chunk) < BUFFER_SIZE:
        #     break
        chunk = client_socket.recv(BUFFER_SIZE)
        bytes_recd = len(chunk)
        chunks.append(chunk)
        # print(f">>> chunk len: {len(chunk)} chunks: {chunks}")
        
        # print(f"2 +++ {chunk}, len {len(chunk)}")
        
    print("outside")
    received_message = b''.join(chunks)
    if received_message.decode().strip().upper() in ['END', 'QUIT', 'EXIT']:
        break
    print("Server says: {}".format(received_message.decode()))

client_socket.close()
