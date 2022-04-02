from time import *
from threading import Thread

def myBox(delay):
    while True:
        print('.......My Box is open')
        sleep(delay)
        print('.......My Box is Closed')
        sleep(delay)
def myLED(delay):
    while True:
        print('My LED is On')
        sleep(delay)
        print('My LED is Off')
        sleep(delay)
delaybox=5
delayled=1
boxThread=Thread(target=myBox, args=(delaybox,))# if i have one argument I need a trailing coma. More than one, NO trailing coma. Weird.
LEDThread=Thread(target=myLED, args=(delayled,))
boxThread.daemon=True
LEDThread.daemon=True
boxThread.start()
LEDThread.start()
j=0
while True:
    print(j)
    j=j+1
    sleep(.1)

