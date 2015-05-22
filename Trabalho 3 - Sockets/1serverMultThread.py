import socket
import threading
import struct
import string

HOST  = '192.168.1.194'
PORTA = 10000

class clientThread(threading.Thread):
	def __init__(self, serv):
		threading.Thread.__init__(self)
		self.server = serv
		self.clientList = []
		self.running = True
		print("Client thread created. . .")
	def run(self):
		print("Beginning client thread loop. . .")
		while self.running:
			for client in self.clientList:
				message = client.sock.recv(self.server.BUFFSIZE)
				message = message.decode('utf-8')
				if message != None and message != "":
					client.update(message)

class clientObject(object):
	def __init__(self,clientInfo):
		self.sock = clientInfo[0]
		self.address = clientInfo[1]
	def update(self,message):
		self.sock.send(message.encode())

class Server(object):
	def __init__(self):
		self.HOST = HOST
		self.PORT = PORTA
		self.BUFFSIZE = 1024
		self.ADDRESS = (self.HOST,self.PORT)
		self.clientList = []
		self.running = True
		self.serverSock = socket.socket()
		self.serverSock.bind(self.ADDRESS)
		self.serverSock.listen(2)
		self.clientThread = clientThread(self)
		print("Starting client thread. . .")
		self.clientThread.start()
		print("Awaiting connections. . .")
		while self.running:
			clientInfo = self.serverSock.accept()
			print("Client connected from {}.".format(clientInfo[1]))
			self.clientThread.clientList.append(clientObject(clientInfo))

		self.serverSock.close()
		print("- end -")

serv = Server()