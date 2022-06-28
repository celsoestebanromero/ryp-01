import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
client = socket.socket()
HEADER_SIZE = 1024

client.connect((IP,PORT))
while True:
    msg = input("Ingrese un mensaje ")
    bitemsg = msg.encode('utf-8')
    REAL_SIZE = str(len(msg)).encode('utf-8') #muestra cuantos bites ocupa el mensaje y lo codifica en bites
    SQUARE_SIZE = len(REAL_SIZE)
    cuenta = REAL_SIZE + b" " * (HEADER_SIZE - SQUARE_SIZE)
    client.send(cuenta) #envía el tamaño del mensaje
    client.send(bitemsg) #envía el mensaje
    if bitemsg == "close":
        socket.close ()
