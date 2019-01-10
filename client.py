import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
mensagemLida = input('Digite a mensagem que deseja enviar: ')
mensagemLidaBytes = str.encode(mensagemLida) #transformar string para byte
type(mensagemLidaBytes) #tranformanto string para byte


try:
	
	print('Enviando {!r}'.format(mensagemLidaBytes))
	sent = sock.sendto(mensagemLidaBytes, server_address)

	
finally:
	print('Fechando socket')
	sock.close()
