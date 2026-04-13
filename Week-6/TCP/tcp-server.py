from socket import *

serverPort = 12000

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the socket to port
serverSocket.bind(('', serverPort))

# listen for incoming connections
serverSOcket.listen(5)
print('Server siap menerima koneksi client...')

running = True
while running: 