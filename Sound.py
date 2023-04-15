import winsound

def down():
    winsound.PlaySound(r"C:\Windows\Media\Speech Misrecognition.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def up():
    winsound.PlaySound(r"C:\Windows\Media\Windows Default.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def end():
    winsound.PlaySound(r"C:\Windows\Media\tada.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

if __name__ == "__main__":
    import time
    down()
    time.sleep(1)
    up()
    time.sleep(1)
    end()