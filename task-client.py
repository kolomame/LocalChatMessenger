import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './data/temp/task-socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)

except socket.eeror as err:
    print(err)

    sys.exit(1)

try:
    message = input('pLease enter the message you want to send.')
    b_message = message.encode()
    sock.sendall(b_message)
    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print('Server response: ' + data)
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()