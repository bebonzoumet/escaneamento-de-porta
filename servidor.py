import scapy.all as scapy
import socket

ip_local = "192.168.0.17"
local_port = 12000
buffer = 1024

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_socket.bind((ip_local,local_port))

print("O servidor UDP está escutando.......")

msg_encoded = serv_socket.recvfrom(buffer)
addr = msg_encoded[1]
print("Mensagem recebida de:", addr)
msg = msg_encoded[0].decode()
serv_socket.sendto(msg.upper().encode(), addr)
print("Resposta enviada para:", addr)
