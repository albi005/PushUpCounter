import Camera
import Count
import cv2
import Lamp
import Mouse
import Sound
import time
import Vision

credits = 0

while True:
    with Camera.Camera() as camera:
        Lamp.on()
        vision = Vision.Vision()
        mouse = None

        while True:
            img = camera.getScreen()

            result = vision.process(img)

            if result.state != Vision.StateChange.NONE:
                credits += .5
                if credits == 5:
                    Sound.end()
                elif result.state == Vision.StateChange.UP:
                    Sound.up()
                else:
                    Sound.down()

            cv2.imshow('Pushup counter', img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

            print(credits)
            if credits >= 5:
                if mouse is None:
                    mouse = Mouse.Mouse()
                if mouse.hasMoved():
                    break

    Count.save(credits)
    cv2.destroyAllWindows()
    Lamp.off()

    while credits > 0:
        print(credits)
        time.sleep(60)
        credits -= .5