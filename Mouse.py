import pyautogui
import math

class Mouse:
    def __init__(self):
        self.position = pyautogui.position()

    def hasMoved(self):
        distance = math.sqrt((self.position.x - pyautogui.position().x)**2 + (self.position.y - pyautogui.position().y)**2)
        return distance > 10