import socket
import threading

# "5 . . . ."
# "H E L L O"
HEADER = 64

PORT = 5050 # just pick an inactive port shouldbe fine

#SERVER = "192.168.1.156" 
# use ifconfig choose ipv4
SERVER = socket.gethostbyname(socket.gethostname())

#SERVER = '<broadcast>'
ADDR = (SERVER, PORT)
FORMAT= 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create different socket, (family, type)


server.bind(ADDR)
def handle_client(conn,addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # blocking code, receive how many byte to receive
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False
            print(f'[{addr}] {msg}')
            conn.send("MSG received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        #socket object   
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start()
        print(f'[ACTIVE Connection]{ threading.activeCount()-1}')


print("[START] server is starting")
start()



