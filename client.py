import socket

_list = ['hour', 'seconds', 'minutes', 'stop']
_input = input('Enter request(hour, seconds, minutes, stop): ')

while _input.lower() not in _list:
    _input = input('Enter request(hour, seconds, minutes, stop): ')

with socket.create_connection(('127.0.0.1', 10001)) as sock:
    sock.settimeout(2)
    try:
        sock.sendall(_input.encode('utf-8'))
    except socket.timeout():
        print('TIMEOUT')
    except socket.error as err:
        print('Send data error', err)
    sock.close()
