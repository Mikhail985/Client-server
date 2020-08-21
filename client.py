import socket, threading

bool1 = False
bool2 = False
server = ('127.0.0.1', 1228)
host = '127.0.0.1'
port = 0

def receiving (self, sock):
    while not bool2:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(bytes.decode(data, encoding='utf-8'))
        except:
            pass

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
sock.setblocking(0)

r = threading.Thread(target = receiving, args = ('RecvTread',sock))
r.start()

name = input('Введите ваше имя: ')

while bool2 == False:
    if bool1 == False:
        sock.sendto((name + ' присоединился к нам').encode('utf-8'),server)
        bool1 = True
    else:
        try:
            message = input()
            sock.sendto((name + ': ' + message).encode('utf-8'), server)
        except:
            sock.sendto((name + 'Покинул чат').encode('utf-8'), server)
            bool2 = True

r.join()
sock.close()

