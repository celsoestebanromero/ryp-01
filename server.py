import socket

IP = socket.gethostbyname(socket.gethostname()) # obtiene la dirección IP por nombre
PORT = 8000 # es un canal de comunicación
server = socket.socket() # el primer socket es el módulo, del cual pido extraer socket

server.bind((IP,PORT)) # ata al servidor a las direcciones
server.listen() # espera a una conexión
print(f"server levantado en {IP}")
conn, addr = server.accept()
print(f"Nueva conexion en {addr}")

while True:
    cuenta = conn.recv(1024) #cantidad de bits que puedo recibir de golpe
    cuenta = cuenta.decode('utf-8') #decodifico la variable
    cuenta = int(cuenta) #convierto el string en entero
    #cuenta_int = len (cuenta) #convierto lo decodificado en un entero
    msg = conn.recv(cuenta).decode('utf-8')
    print(f"Cliente dijo: {msg}")
    if msg == "close":
        break
