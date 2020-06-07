# Timew

Interact with timewarrior directly from i3blocks. Show current task time when
active. A floating window allows to inpute the task name.

![no active task](i3blocks-timew-01.png)
![floating windows to input task name](i3blocks-timew-02.png)
![active task, time tracking](i3blocks-timew-03.png)

# Config

##i3blocks

```
[timew]
command=python3 ~/.config/i3blocks/timew/timew.py
interval=10
signal=10
```

##i3

In order to have a floating window with i3.

```
# for python easygui
for_window [title="task" class="Tk"] floating enable
```
