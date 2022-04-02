import time
def myBox():
    while True:
        print('.......My Box is open')
        time.sleep(5)
        print('.......My Box is Closed')
        time.sleep(5)
def myLED():
    while True:
        print('My LED is On')
        time.sleep(1)
        print('My LED is Off')
        time.sleep(1)
myBox()
myLED()
