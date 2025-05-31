#Librarires
import socket
import pythonosc
import speech_recognition as sr
import pyaudio
from client import Client
from test.test_asdl_parser import src_base

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

    print("Step 1 done")
    #Step 2
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    client = Client(53000,ip)

    print("Step 2 done")
    #Step 2.5
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print(r.recognize_amazon(audio))

    print("Step 2.5 done")

    #Step 3


main()
