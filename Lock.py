import pygetwindow as gw
import pyautogui

class Lock:
    def __init__(self):
        pass

windows = gw.getAllWindows()
for window in windows:
    print(window.title)