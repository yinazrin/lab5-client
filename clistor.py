import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("please run >>  python3 clientStore.py < server ip address > \n\n")
    exit(1)


s = socket.socket()

PORT = 9898

s.connect((ServerIp, PORT))

filetosend = input('\nEnter the file name to be stored in server: ')     
s.send(filetosend.encode())                     
file = open(filetosend, "rb")                   

SendData = file.read(99999)

while SendData:
    print("\n>Message received from the server:", s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(99999)
    print(">" + filetosend + " has been copied successfully to the server for storage.\n")
    
s.close()
