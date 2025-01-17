import socket
import pythonosc
import speech_recognition

from client import Client


#Steps to develop
#1 - Open a file and add each line of the file to an array
#2 - Create a Client
#2.5 - Create microphone and listener
#3 - Loop through each line. If the word is spoken, GO (/workspace/{id}/go), otherwise wait .01

def main():
    #Step 1
    file = open("lines.txt", "r")
    lines = []

    for line in file:
        lines.append(line)

    #Step 2
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    client = Client(53000,ip)

    #Step 3


main()