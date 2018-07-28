import socket

def port_select(validated_data):
    data = validated_data
    sock = socket.socket()
    sock.bind(('', 0))
    data['port'] = sock.getsockname()[1]
    sock.close()
    return data
