#!/usr/bin/python3

import os
import pathlib
import easygui
import subprocess

def start():
    myvar = easygui.enterbox("What task will you be working on? ", 'task')
    if (myvar != None):
        os.system('timew start ' + myvar +' > /dev/null')

def stop():
    os.system('timew stop > /dev/null')

def left_click():
    start()

def right_click():
    stop()

#Personnaly I don't use middle click
def middle_click():
    pass

def get_status():
    current_dir = pathlib.Path(__file__).parent
    print(subprocess.getoutput("bash "+str(current_dir)+ "/timew.sh"))

def main():
    if os.environ.get('BLOCK_BUTTON') == "1":
        left_click()
    if os.environ.get('BLOCK_BUTTON') == "2":
        middle_click()
    if os.environ.get('BLOCK_BUTTON') == "3":
        right_click()

    get_status()

if __name__ == "__main__":
    main()
