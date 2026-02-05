import event, time, cyberpi, mbot2

# initialise speech recognition
cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")

# initialise text-to-speech
cyberpi.driver.cloud_translate.TTS_URL = "{TTSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")

# if button A is pressed, stop the robot and clear the console
@event.is_press('a')
def is_btn_press():
    cyberpi.stop_other()
    cyberpi.console.clear()

# if button B is pressed, connect to wifi and listen for speech commands
@event.is_press('b')
def is_btn_press1():
    cyberpi.wifi.connect('ssid', 'password')
    while not cyberpi.controller.is_press('a'): # keep listening until button A is pressed
        if cyberpi.wifi.is_connect():
            cyberpi.cloud.listen('english', 1)
            text_to_speech(cyberpi.cloud.listen_result())
        else:
            cyberpi.console.println('Waiting to connect to Wifi...')
    
    cyberpi.console.clear()

# convert recognised speech commands into movement commands for the robot
def text_to_speech(speech_result):
    cyberpi.cloud.tts('en', speech_result)
