import socket
import sys
import traceback

BUFFER_SIZE = 16

def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    # sock.connect(server_address)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.
    sock.connect(server_address)

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.
        sock.sendall(msg.encode('utf-8'))
        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems
        chunk = ''
        chunks = []
        bytes_recd = BUFFER_SIZE
        while bytes_recd >= BUFFER_SIZE:
            chunk = sock.recv(BUFFER_SIZE)
            bytes_recd = len(chunk)
            chunks.append(chunk)
            # print(f"chunk len {bytes_recd}, chunk {chunks}")

        # print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        received_message = b''.join(chunks)
        # print(f" received from server: {received_message}")
        print('closing socket', file=log_buffer)

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
        sock.close()
        return received_message.decode()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    recv = client(msg)
    print(f'receiving: "{recv}"')
