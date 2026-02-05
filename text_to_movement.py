import event, time, cyberpi, mbot2

# initialise speech recognition
cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")

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
            text_to_movement(cyberpi.cloud.listen_result())
        else:
            cyberpi.console.println('Waiting to connect to Wifi...')

    cyberpi.console.clear()

# convert recognised speech commands into movement commands for the robot
def text_to_movement(speech_result):
    speech_lower = str(speech_result).lower()
    
    if 'forward' in speech_lower:
        mbot2.forward(50, 1)
    elif 'backward' in speech_lower:
        mbot2.backward(50, 1)
    elif 'left' in speech_lower:
        mbot2.turn_left(50, 1)
    elif 'right' in speech_lower:
        mbot2.turn_right(50, 1)
    else:
        cyberpi.console.println('Command not recognized.')