import socket
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

SERVER = None
PORT = 8000
IP_ADDRESS =  "192.168.133.189"
screen_width = None
screen_height = None

keyboard = Controller()

def acceptConnections():
    global SERVER
    while True:
        client_socket,addr = SERVER.accept()
        print(f"Connection established with{client_socket}:{addr}")

def getDeviceSize():
    global screen_height
    global screen_width
    for m in get_monitors():
         screen_width = int(str(m).split(",")[2].strip().split('width=')[1])
         screen_height = int(str(m).split(",")[3].strip().split('height=')[1])
      
def setup():
    print("\n\t\t\t\t\t*** Welcome To Remote Mouse ***\n")
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)
    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...\n")
    getDeviceSize()
    acceptConnections()
setup()