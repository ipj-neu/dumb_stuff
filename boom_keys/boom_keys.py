import keyboard
from pygame import mixer
import sys
import os

mixer.init()
sound = mixer.Sound(os.path.join(sys._MEIPASS, "resources", "vine-boom.mp3"))

def call(event):
    sound.play()

keyboard.on_press(call)

keyboard.wait("ctrl + alt + n")