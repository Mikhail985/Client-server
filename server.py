import socket

host = '127.0.0.1'
port = 1228
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))

bool = True
clients = []

print("Запуск")

while bool == True:
    try:
        data, addr = sock.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
          
        print(str(addr[1]) + ' :' + data.decode())
        
        for client in clients:
            if addr != client:
                sock.sendto(data, client)
    except:
        print('Конечная')
        bool = False

sock.close()