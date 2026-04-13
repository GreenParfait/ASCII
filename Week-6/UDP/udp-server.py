from base64 import decode
from socket import *

# Pembuatan Socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind
serverSocket.bind(
    # Tipe data tuple
    ('', serverPort)
)

print("[SERVER] siap digunakan")

running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048)
    # message yang diterima = 10101001
    decodedMessage = message.decode()

    if decodedMessage.lower() == "exit":
        print("[SYSTEM] Server telah diberhentikan")
        running = False
        continue

    # CAPSLOCK
    modifiedMessage = decodedMessage.upper()
    print("[SERVER] diterima dari  ", clientAddress, " message: ", decodedMessage)

    # Mengirim ke client
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] socket server telah ditutup")