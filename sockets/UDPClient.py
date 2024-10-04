# -*- coding: cp1252 -*-
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Recebe mensagem do usuario e envia ao destino
message = input('Digite uma frase:')
clientSocket.sendto(message.encode('ascii'),(serverName, serverPort))

#Aguarda mensagem de retorno e a imprime
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Retorno do Servidor:"+modifiedMessage.decode())

clientSocket.close()
