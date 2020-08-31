import socket

PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSEGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = client.recv(1024)
print(msg.decode(FORMAT))
