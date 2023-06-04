## Python Server

# import Socket
import socket
import subprocess

# Connection Create Socket TCP Used
Craete_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Craete_Socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

# Baind IP and PORT
Craete_Socket.bind(("192.168.230.135",8080))
# Watting clinet request
print("[+] Listening....")
Craete_Socket.listen(1)

# Accept data
Clinte,addr = Craete_Socket.accept()
print("Connected") 

# Clinte data send
# Clinte.send(b"root")
while True:
    # Clinte inpute 
    Cmd = input("$ ")
    if Cmd == "exit":
        break
    else:
        Clinte.send(Cmd.encode())
        Output = (Clinte.recv(1024)).decode()
        print(Output)