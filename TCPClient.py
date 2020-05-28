
from socket import *

serverName = gethostname()
serverPort = 12000


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Type lowercase sentence\n')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())
clientSocket.close()
input('End')