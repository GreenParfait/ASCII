from runpy import _ModifiedArgv0
from socket import *


serverName = 'localhost'
serverPort = 8080

# Mmebuat client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to Server
clientSocket.connect(())

# send message to server
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())

# receive modified message from server
modifiedSentence = clientSocket.recv(2048)
print('From server: ', modifiedSentence.decode())

# close the socket
clientSocket.close()