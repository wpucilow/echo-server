import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address =  ('127.0.0.1', 20000)
sock.bind(server_address)
# print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
print('starting up on {} port {}'.format(*sock.getsockname()), file=sys.stderr)
sock.listen(2)

while True:
    # print >>sys.stderr, 'waiting for a connection'
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        # print >>sys.stderr, 'client connected:', client_address
        print("client connected: {}".format(client_address), file=sys.stderr)
        while True:
            data = connection.recv(16)
            # print >>sys.stderr, 'received "%s"' % data
            if data:
                print("received: {}".format(*data), file=sys.stderr)
                connection.sendall(data)
            elif data.decode().strip().upper() in ['END', 'QUIT', 'EXIT']:
                break
            else:
                break
    finally:
        connection.close()