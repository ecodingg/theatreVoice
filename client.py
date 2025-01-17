import socket
import pythonosc

#Client class
class Client():
    #Initialize Class
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    #Send Signal
    def sendSignal(self):
        print("HELP")

