from base64 import decode
from socket import *

# jaringan yang kita hubungkan akan otomatis jadi local host
serverName = "localhost"
serverPort = 12000 # Port connection

# AF_INET = ip addr v4 | Sock_DGRAM = UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# If running = true, program akan tetap berjalan
running = True
while running:
    message = input("> ") #Input dari user

    # Kondisi untuk keluar.
    if message.lower() == "exit":

        # Mengirimkan pesan Exit
        clientSocket.sendto(
        message.encode(),
        (serverName, serverPort),
        )

        print("[SYSTEM] akan keluar dari program")
        running = False
        continue

    
    #abc, Namaku, miaw, kucing, anjing, untuk mengirim pesan
    clientSocket.sendto(
        message.encode(),
        (serverName, serverPort)
    )

    # Menerima Pesan
    modifiedMessage, serverAddress = clientSocket. recvfrom(2048)

    print("[SYSTEM] Pesan telah diterima dari: ", serverAddress)
    print(modifiedMessage.decode()) # 101010010101010101

clientSocket.close()
print("[SYSTEM] Connection telah ditutup.")
