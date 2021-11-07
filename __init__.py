from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import serial
import time
import subprocess
import decimal

class ThumbsSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler('thumbs.intent')
    def handle_not_are_you_intent(self, message):
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        ser.write(b"thumb")
        time.sleep(1.5)
        self.speak_dialog("hello knight")
      

    def stop(self):
        pass

def create_skill():
    return ThumbsSkill()
