from socket import *

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

treat = {
	'U': lambda x: x.upper(), # U <text>
	'L': lambda x: x.lower()  # L <text>
}

while 1:
	try:
	   #Cria um socket para tratar a conexao do cliente
	   connectionSocket, addr = serverSocket.accept()
	   msg = connectionSocket.recv(1024).decode()

	   try:
		   command, sentence = msg.split(' ',1)
		   if len(command)>1: 
			   raise IndexError
		   returnMsg = treat[command](sentence)
	   except (IndexError, ValueError):
		   returnMsg = "ERR1"
	   except (KeyError):
	   	   returnMsg = "ERR2"
	   
	   connectionSocket.send(returnMsg.encode('ascii'))
	   connectionSocket.close()
	except (KeyboardInterrupt, SystemExit):
		break

serverSocket.shutdown(SHUT_RDWR)
serverSocket.close()
