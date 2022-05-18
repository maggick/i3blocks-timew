#!/usr/bin/python3

import os
import pathlib
import easygui
import subprocess
from tasklib import TaskWarrior

def start():
    w = TaskWarrior()
    tasks = w.tasks.pending()
    tasks_r = []
    for task in tasks:
        tasks_r.append(str(task['id']) + ": " +task['project'] + ": " +task['description'])

    msg="What task will you be working on?"
    title="task"
    myvar = None
    if len(tasks_r) !=0:
      if len(tasks_r) ==1: # easygui choicebox want at least two options
        tasks_r.append("")
      myvar = easygui.choicebox(msg, title, tasks_r)

    if (myvar != None and myvar != "Add more choices"):
        os.system("task start " + str(myvar).split(':')[0] +"")

    if (myvar == None or myvar == "Add more choices"):
        myvar = easygui.enterbox(msg, title)
        if (myvar != None):
            os.system('timew start ' + myvar +' > /dev/null')

def stop():
    w = TaskWarrior()
    tasks = w.tasks.pending()
    for task in tasks:
        os.system('task stop ' + str(task['id']))
    os.system('timew stop')

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
