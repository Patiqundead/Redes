import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#HOST  = 'localhost'
HOST  = '172.20.72.55'
PORTA = 10000
server_address = (HOST, PORTA)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
	# Send data
	#message = 'This is the message.  It will be repeated.'
	message = input('Client>')
	print ('Client: sending "%s"' % message)
	
	sock.sendall(message.encode('utf-8'))

	# Look for the response
	#amount_received = 0
	#amount_expected = len(message)
	data = ''
	while True: #jogando
		data = sock.recv(1024)
		data = data.decode('utf-8')
		
		if data != "FIM":
			print ('Client: received\n%s' % data)
		else:
			#jogador X venceu ou voce perdeu/ganhou
			break
		data = ''
		
		message = ''
		while not message:
			message = input('Entrada> ')
			if message != "":
				print ('Client: sending "%s"' % message)
				sock.sendall(message.encode('utf-8'))
				if message == 'FIM':
					break
				message = ''
				break

finally:
	print ('closing socket')
	sock.close()