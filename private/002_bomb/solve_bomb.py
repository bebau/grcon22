#!/usr/bin/env python


import time
import bombbb   

def success_message():
    print("YOU HAVE CAPTURED THIS FLAG!! ENTER {the code you used to defuse the bomb}")
    print("This message will self destruct in 60 seconds...")

tries = 0
result = 0
while tries < 10:
    result = bombbb.bomb1()
    if result == bombbb._SUCCESS:
        success_message()
        time.sleep(60)
    else:
        if tries == 0 and result != bombbb._HELP:
            print("Just this once, I will be nice. Try entering 'hint' or 'help'.")
        tries += 1
else:
    with open("bombbb.pyc", "w") as f:
        f.write("the bomb exploded :(")

