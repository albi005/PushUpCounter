import pygetwindow as gw
import time
import os
import numpy as np
import cv2
from mss import mss

pixymon = None

def initialize():
    global pixymon
    windows = gw.getWindowsWithTitle('PixyMon')
    if len(windows) == 0:
        os.startfile(r'C:\Program Files (x86)\PixyMon\bin\PixyMon.exe')
        while len(windows) == 0:
            windows = gw.getWindowsWithTitle('PixyMon')
            time.sleep(0.1)
    pixymon = gw.getWindowsWithTitle('PixyMon')[0]
    pixymon.moveTo(-800, 0)
    pixymon.resizeTo(800, 700)

sct = mss()

def getScreen():
    ensureWindowLayout()

    bounding_box = (pixymon.left + 12, pixymon.top + 100, pixymon.left + pixymon.width - 12, pixymon.top + pixymon.height - 116)
    sct_img = sct.grab(bounding_box)
    img = np.array(sct_img)
    return img

def ensureWindowLayout():
    global pixymon
    windows = gw.getWindowsWithTitle('Pushup counter')
    if len(windows) != 0:
        window = windows[0]
        
        if window.left != -1920 or window.top != 0:
            window.moveTo(-1920, 0)

    if pixymon.left != -960 or pixymon.top != 0:
        pixymon.moveTo(-960, 0)
        pixymon.resizeTo(960, 800)

if __name__ == '__main__':
    initialize()
    while True:
        img = getScreen()
        cv2.imshow('Pushup counter', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break