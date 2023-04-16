import pygetwindow as gw
import time
import numpy as np
import cv2
from mss import mss
import subprocess

class Camera:
    def __init__(self):
        self.sct = mss()

    def __enter__(self):
        self.process = subprocess.Popen(r'C:\Program Files (x86)\PixyMon\bin\PixyMon.exe')
        while len(gw.getWindowsWithTitle('PixyMon')) == 0:
            time.sleep(0.1)
        self.pixymon = gw.getWindowsWithTitle('PixyMon')[0]
        self.pixymon.moveTo(-800, 0)
        self.pixymon.resizeTo(800, 700)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.process.kill()

    def getScreen(self):
        self.ensureWindowLayout()
        pixymon = self.pixymon
        bounding_box = (pixymon.left + 12, pixymon.top + 100, pixymon.left + pixymon.width - 12, pixymon.top + pixymon.height - 116)
        sct_img = self.sct.grab(bounding_box)
        img = np.array(sct_img)
        return img

    def ensureWindowLayout(self):
        windows = gw.getWindowsWithTitle('Pushup counter')
        if len(windows) != 0:
            window = windows[0]
            target = (960 - int(window.width / 2), 540 - int(window.height / 2))
            if window.topleft != target:
                window.moveTo(target[0], target[1])

        pixymon = self.pixymon
        if pixymon.left != -960 or pixymon.top != 0:
            pixymon.moveTo(-960, 0)
            pixymon.resizeTo(960, 800)

if __name__ == '__main__':
    with Camera() as camera:
        while True:
            img = camera.getScreen()
            cv2.imshow('Pushup counter', img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    input('Press enter to exit')