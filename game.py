from pynput import keyboard
import datetime
import time
import random

key_pressed = False
gameStart = True
keys = ['Q', 'W', 'E', 'R', 'T', 'Y', 'Z']




class keyLogger:
    @staticmethod
    def on_press(key):
        global start_time
        global key_pressed
        if key_pressed == False:
            start_time = datetime.datetime.now().microsecond
            key_pressed = True
            try:
                print('alphanumeric key {0} pressed'.format(
                key.char))
            except AttributeError:
                print('special key {0} pressed'.format(
                    key))
        else:
            key_pressed = True

    def on_release(key):
        global end_time
        global key_pressed
        end_time = datetime.datetime.now().microsecond
        key_pressed = False
        print('Key pressed for: ', end_time - start_time)
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
 
listener = keyboard.Listener(
        on_press=keyLogger.on_press,
        on_release=keyLogger.on_release,)


while gameStart:
    correct_key = random.choice(keys)
    print(correct_key, end='\r')
    while True:
            pressed_key = listener.wait()  # Wait for a key press event
            if pressed_key is not None:  # Check if a key was pressed
                break  

    if pressed_key.char == correct_key:
        print("Correct!")

    elif pressed_key == keyboard.Key.esc:
        print("Quitting...")
        break  # Exit the loop

    else:
        print("Wrong key. Try again.")

   
