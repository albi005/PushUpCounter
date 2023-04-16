from enum import Enum
import cv2
import numpy as np
import PoseModule as pm
import numpy as np

class StateChange(Enum):
    NONE = 0
    UP = 1
    DOWN = 2

class VisionResult:
    def __init__(self, img, state: StateChange):
        self.img = img
        self.state = state

class Vision:
    def __init__(self):
        self.detector = pm.poseDetector()
        self.count = 0
        self.direction = 0
        self.form = 0
        self.feedback = "Fix Form"
    
    def process(self, img) -> VisionResult:
        img = self.detector.findPose(img, False)
        lmList = self.detector.findPosition(img, True)

        state = StateChange.NONE

        if len(lmList) != 0:
            elbow = self.detector.findAngle(img, 11, 13, 15)
            shoulder = self.detector.findAngle(img, 13, 11, 23)
            hip = self.detector.findAngle(img, 11, 23,25)
            
            #Percentage of success of pushup
            per = np.interp(elbow, (90, 160), (0, 100))
            
            #Bar to show Pushup progress
            bar = np.interp(elbow, (90, 160), (380, 50))

            #Check to ensure right form before starting the program
            if elbow > 160 and shoulder > 40 and hip > 160:
                self.form = 1
        
            #Check for full range of motion for the pushup
            if self.form == 1:
                if per == 0:
                    if elbow <= 90 and hip > 160:
                        self.feedback = "Up"
                        if self.direction == 0:
                            self.count += 0.5
                            self.direction = 1
                            state = StateChange.UP
                    else:
                        self.feedback = "Fix Form"
                        
                if per == 100:
                    if elbow > 160 and shoulder > 40 and hip > 160:
                        self.feedback = "Down"
                        if self.direction == 1:
                            self.count += 0.5
                            self.direction = 0
                            state = StateChange.DOWN
                    else:
                        self.feedback = "Fix Form"
                        # form = 0

            #Draw Bar
            if self.form == 1:
                cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                            (255, 0, 0), 2)

            #Pushup counter
            cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(self.count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            #Feedback 
            cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.feedback, (500, 40 ), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 255, 0), 2)

        return VisionResult(img, state)
