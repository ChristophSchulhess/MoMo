'''  Define hooks called in APIView methods such as perform_create() '''

import socket

# Select a random free port (let the low-level network functionality decide)
def port_select(validated_data):
    data = validated_data
    sock = socket.socket()
    sock.bind(('', 0))
    data['port'] = sock.getsockname()[1]
    sock.close()
    return data
