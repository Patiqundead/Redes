import socket
import sys
import random

def fazJogada(matriz, pos, vezQuemJoga, posicoesJogadas):
	jogada = 1
	if (pos == '1' or pos == 1) and matriz[0][0] == ' ':
		if vezQuemJoga == 1:
			matriz[0][0] = 'X'
		else:
			matriz[0][0] = 'O'
			
	elif (pos == '2' or pos == 2) and matriz[0][2] == ' ':
		if vezQuemJoga == 1:
			matriz[0][2] = 'X'
		else:
			matriz[0][2] = 'O'	
		
	elif (pos == '3' or pos == 3) and matriz[0][4] == ' ':
		if vezQuemJoga == 1:
			matriz[0][4] = 'X'
		else:
			matriz[0][4] = 'O'
		
	elif (pos == '4' or pos == 4) and matriz[2][0] == ' ':
		if vezQuemJoga == 1:
			matriz[2][0] = 'X'
		else:
			matriz[2][0] = 'O'
		
	elif (pos == '5' or pos == 5) and matriz[2][2] == ' ':
		if vezQuemJoga == 1:
			matriz[2][2] = 'X'
		else:
			matriz[2][2] = 'O'
		
	elif (pos == '6' or pos == 6) and matriz[2][4] == ' ':
		if vezQuemJoga == 1:
			matriz[2][4] = 'X'
		else:
			matriz[2][4] = 'O'
		
	elif (pos == '7' or pos == 7) and matriz[4][0] == ' ':
		if vezQuemJoga == 1:
			matriz[4][0] = 'X'
		else:
			matriz[4][0] = 'O'
		
	elif (pos == '8' or pos == 8) and matriz[4][2] == ' ':
		if vezQuemJoga == 1:
			matriz[4][2] = 'X'
		else:
			matriz[4][2] = 'O'
		
	elif (pos == '9' or pos == 9) and matriz[4][4] == ' ':
		if vezQuemJoga == 1:
			matriz[4][4] = 'X'
		else:
			matriz[4][4] = 'O'
		
	else:
		#posição não pode ser jogada
		jogada = 0
	posicoesJogadas = verificaMatriz(matriz)
	return matriz, jogada, posicoesJogadas
	
def verificaMatriz(matriz):
	posicoesJogadas = 0
	if matriz[0][0] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[0][2] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[0][4] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[2][0] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[2][2] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[2][4] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[4][0] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[4][2] != ' ':
		posicoesJogadas = posicoesJogadas + 1
	if matriz[4][4] != ' ':
		posicoesJogadas = posicoesJogadas + 1		
	return posicoesJogadas
	
def iniMatriz(matriz):
	matriz.append([' ', '|', ' ', '|', ' '])
	matriz.append(['-', '+', '-', '+', '-'])
	matriz.append([' ', '|', ' ', '|', ' '])
	matriz.append(['-', '+', '-', '+', '-'])
	matriz.append([' ', '|', ' ', '|', ' '])
	return matriz

def testaPosicao(matriz, jogador):
	if jogador == 1:
		Vantagem = "X"
		Desvantagem = "O"
	elif jogador == 2:
		Vantagem = "O"
		Desvantagem = "X"
		
	posParaJogar = 0
	
	if (matriz[0][0] == Vantagem and matriz[0][2] == Vantagem and matriz[0][4] != Desvantagem): #primeira linha
		posParaJogar = 3
	elif (matriz[0][0] == Vantagem and matriz[0][2] != Desvantagem and matriz[0][4] == Vantagem): #primeira linha
		posParaJogar = 2
	elif (matriz[0][0] != Desvantagem and matriz[0][2] == Vantagem and matriz[0][4] == Vantagem): #primeira linha
		posParaJogar = 1
		
	elif (matriz[2][0] == Vantagem and matriz[2][2] == Vantagem and matriz[2][4] != Desvantagem): #segunda linha
		posParaJogar = 6
	elif (matriz[2][0] == Vantagem and matriz[2][2] != Desvantagem and matriz[2][4] == Vantagem): #segunda linha
		posParaJogar = 5
	elif (matriz[2][0] != Desvantagem and matriz[2][2] == Vantagem and matriz[2][4] == Vantagem): #segunda linha
		posParaJogar = 4
		
	elif (matriz[4][0] == Vantagem and matriz[4][2] == Vantagem and matriz[4][4] != Desvantagem): #terceira linha
		posParaJogar = 9
	elif (matriz[4][0] == Vantagem and matriz[4][2] != Desvantagem and matriz[4][4] == Vantagem): #terceira linha
		posParaJogar = 8
	elif (matriz[4][0] != Desvantagem and matriz[4][2] == Vantagem and matriz[4][4] == Vantagem): #terceira linha
		posParaJogar = 7
		
	elif (matriz[0][0] == Vantagem and matriz[2][0] == Vantagem and matriz[4][0] != Desvantagem): #primeira coluna
		posParaJogar = 7
	elif (matriz[0][0] == Vantagem and matriz[2][0] != Desvantagem and matriz[4][0] == Vantagem): #primeira coluna
		posParaJogar = 4
	elif (matriz[0][0] != Desvantagem and matriz[2][0] == Vantagem and matriz[4][0] == Vantagem): #primeira coluna
		posParaJogar = 1
		
	elif (matriz[0][2] == Vantagem and matriz[2][2] == Vantagem and matriz[4][2] != Desvantagem): #segunda coluna
		posParaJogar = 8
	elif (matriz[0][2] == Vantagem and matriz[2][2] != Desvantagem and matriz[4][2] == Vantagem): #segunda coluna
		posParaJogar = 5
	elif (matriz[0][2] != Desvantagem and matriz[2][2] == Vantagem and matriz[4][2] == Vantagem): #segunda coluna
		posParaJogar = 2
		
	elif (matriz[0][4] == Vantagem and matriz[2][4] == Vantagem and matriz[4][4] != Desvantagem): #terceira coluna
		posParaJogar = 9
	elif (matriz[0][4] == Vantagem and matriz[2][4] != Desvantagem and matriz[4][4] == Vantagem): #terceira coluna
		posParaJogar = 6
	elif (matriz[0][4] != Desvantagem and matriz[2][4] == Vantagem and matriz[4][4] == Vantagem): #terceira coluna
		posParaJogar = 3
		
	elif (matriz[0][0] == Vantagem and matriz[2][2] == Vantagem and matriz[4][4] != Desvantagem): #diagonal principal
		posParaJogar = 9
	elif (matriz[0][0] == Vantagem and matriz[2][2] != Desvantagem and matriz[4][4] == Vantagem): #diagonal principal
		posParaJogar = 5
	elif (matriz[0][0] != Desvantagem and matriz[2][2] == Vantagem and matriz[4][4] == Vantagem): #diagonal principal
		posParaJogar = 1
		
	elif (matriz[0][4] == Vantagem and matriz[2][2] == Vantagem and matriz[4][0] != Desvantagem): #diagonal secundaria
		posParaJogar = 7
	elif (matriz[0][4] == Vantagem and matriz[2][2] != Desvantagem and matriz[4][0] == Vantagem): #diagonal secundaria
		posParaJogar = 5
	elif (matriz[0][4] != Desvantagem and matriz[2][2] == Vantagem and matriz[4][0] == Vantagem): #diagonal secundaria
		posParaJogar = 3
	
	return posParaJogar
	
def IAJoga(matriz, posicoesJogadas):
	posicao = 0
	posicao = testaPosicao(matriz, 2)
	jogada = 0
	if posicao == 0: #não achou posição para ganhar
		print ("Server não ganha\n")
		posicao = testaPosicao(matriz, 1)
		if posicao == 0: #adversario não ganha
			print ("Client não ganha\n")
			while True:
				posicao = random.randrange(9) + 1
				posStr = str(posicao)
				matriz, jogada, posicoesJogadas = fazJogada(matriz, posStr, 2, posicoesJogadas)
				if posicoesJogadas == 9:
					break
				if jogada == 1:
					#print ("jogada com sucesso\n")
					break
		else:
			print ("client ganha\n")
			posStr = str(posicao)
			matriz, jogada, posicoesJogadas = fazJogada(matriz, posicao, 2, posicoesJogadas)
	else:
		print ("server ganha\n")
		posStr = str(posicao)
		matriz, jogada, posicoesJogadas = fazJogada(matriz, posicao, 2, posicoesJogadas)

	jogo = carregaMatriz(matriz)
	print (jogo)
	return matriz
	
def verificaFim(matriz, quemJoga):
	fim = 0 #fim recebe o numero do ganhador 1 - jogador 2 - IA
	if fim == 0: #horizontal
		fim = verificaHorizontal(matriz, quemJoga)
	if fim == 0: #vertical
		fim = verificaVertical(matriz, quemJoga)
	if fim == 0: #diagonal
		fim = verificaDiagonal(matriz, quemJoga)
	return fim

def verificaHorizontal(matriz, quemJoga):
	fim = 0
	XouO = ""
	if quemJoga == 1:
		XouO = "X"
	elif quemJoga == 2:
		XouO = "O"
	
	if matriz[0][0] == XouO and matriz[0][2] == XouO and matriz[0][4] == XouO: # |
		fim = quemJoga
	elif matriz[2][0] == XouO and matriz[2][2] == XouO and matriz[2][4] == XouO: # |
		fim = quemJoga
	elif matriz[4][0] == XouO and matriz[4][2] == XouO and matriz[4][4] == XouO: # |
		fim = quemJoga
	else:
		fim = 0
	return fim
	
def verificaVertical(matriz, quemJoga):
	fim = 0
	XouO = ""
	if quemJoga == 1:
		XouO = "X"
	elif quemJoga == 2:
		XouO = "O"
	
	if matriz[0][0] == XouO and matriz[2][0] == XouO and matriz[4][0] == XouO: # -
		fim = quemJoga
	elif matriz[0][2] == XouO and matriz[2][2] == XouO and matriz[4][2] == XouO: # -
		fim = quemJoga
	elif matriz[0][4] == XouO and matriz[2][4] == XouO and matriz[4][4] == XouO: # -
		fim = quemJoga
	else:
		fim = 0
	return fim
	
def verificaDiagonal(matriz, quemJoga):
	fim = 0
	XouO = ""
	if quemJoga == 1:
		XouO = "X"
	elif quemJoga == 2:
		XouO = "O"
	
	if matriz[0][0] == XouO and matriz[2][2] == XouO and matriz[4][4] == XouO: # \
		fim = quemJoga
	elif matriz[0][4] == XouO and matriz[2][2] == XouO and matriz[4][0] == XouO: # /
		fim = quemJoga
	else:
		fim = 0
	return fim
	
def carregaMatriz(matriz):
	jogo = ''
	jogo = "\n" + str(matriz[0][0]) + "|" + str(matriz[0][2]) + "|" + str(matriz[0][4]) + "\n-+-+-\n" + str(matriz[2][0]) + "|" + str(matriz[2][2]) + "|" + str(matriz[2][4]) + "\n-+-+-\n" + str(matriz[4][0]) + "|" + str(matriz[4][2]) + "|" + str(matriz[4][4])
	return jogo
	
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
#HOST  = 'localhost'
HOST  = '172.20.72.55'
PORTA = 10000
server_address = (HOST, PORTA)
print ('Server: starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)
random.seed()
jogada = 1 #permite fazer jogada
quemJoga = 0
terminou = 0
posicoesJogadas = 0
retorno = ""

while True:
	# Wait for a connection
	print ('Server: waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print ('Server: connection from', client_address)
		quemJoga = 1 #1 - jogador - 2 servidor
		jogada = 1
		matriz = []
		matriz = iniMatriz(matriz)

		while True:
			data = connection.recv(1024)
			data = data.decode('utf-8')
			
			#pega o valor de DATA que contem a posição, informar se o valor é acima de 9 ou abaixo de 1
			if data != "FIM":
				pos = data
				
				while terminou == 0:
					if pos in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 1, 2, 3, 4, 5, 6, 7, 8, 9]:

						if posicoesJogadas == 9:
							terminou = 1 
							retorno = "\nEmpate\n"  + carregaMatriz(matriz)
							break
						if quemJoga == 1 and terminou == 0:
							matriz, jogada, posicoesJogadas = fazJogada(matriz, pos, quemJoga, posicoesJogadas)
							if jogada == 0:
								retorno = '\nPosição já jogada.\n'  + carregaMatriz(matriz)
								break
							fim = 0
							fim = verificaFim(matriz, 1)
							quemJoga = 2
							if fim != 0: #terminou o jogo
								retorno = "\nParabéns! Você venceu. =D\n" + carregaMatriz(matriz)
								terminou = 1
								break
							retorno = ''
							retorno = carregaMatriz(matriz)

						if posicoesJogadas == 9:
							terminou = 1
							retorno = "\nEmpate\n"  + carregaMatriz(matriz)
							break
						if quemJoga == 2 and terminou == 0:
							matriz = IAJoga(matriz, posicoesJogadas)
							fim = 0
							fim = verificaFim(matriz, 2)
							quemJoga = 1
							if fim != 0: #terminou o jogo
								retorno = "\nQue pena! Você perdeu. D=\n"  + carregaMatriz(matriz)
								terminou = 1
								break
							retorno = ''
							retorno = carregaMatriz(matriz)
							break #IA joga, força sair do laço para o client poder jogar
						
					#FimDoIf pos in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
					else:
						retorno = '\nPosição inválida.\n'  + carregaMatriz(matriz)
						break

					if jogada == 0:
						retorno = '\nPosição já jogada.\n'  + carregaMatriz(matriz)
						break
						
					if posicoesJogadas == 9:
						retorno = "\nEmpatou '-'\n"  + carregaMatriz(matriz)
						terminou = 1
						
					if terminou == 1:
						retorno = carregaMatriz(matriz)
						connection.sendall(retorno.encode('utf-8'))
						retorno = "FIM"
						break
					
				#FimDoWhile jogada != 0:
				connection.sendall(retorno.encode('utf-8'))
			#FimDoIf data != "FIM":
			else:
				print ('Server: no more data from', client_address)
				connection.sendall(data.encode('utf-8'))
			#FimDoElse
		#FimDoWhile
	finally:
		# Clean up the connection
		connection.close()
		entrada = ''
		entrada = input("Server>")
		if entrada == "FIM":
			break