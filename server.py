import socket
import sys

#my_decoded_str = my_str_as_bytes.decode()
#type(my_decoded_str) # ensure it is string representation

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print('Iniciando no IP {} e na porta {}'. format(*server_address))
sock.bind(server_address)

while True:
	print('\n Esperando receber a mensagem')
	data, address = sock.recvfrom(4096)
	
	print('recebido {} bytes do IP {}'.format(len(data), address))
	dadosRecebidos = data.decode() #tranformar byte para string
	type(dadosRecebidos) # tranformando byte para string
	print("Recebido: ",dadosRecebidos)
	

