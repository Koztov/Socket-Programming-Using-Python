# client code
from socket import *

HOST = 'localhost'
PORT = 8000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    message = raw_input("Message: ")
    s.send(message)
    print "Arriving reply"
    reply = s.recv(1024)
    print "Replay is ", repr(reply)

s.close()
