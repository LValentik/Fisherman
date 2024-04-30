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
press = keyLogger.on_press
release = keyLogger.on_release

listener = keyboard.Listener(press, release)
listener.start()


while gameStart:
    correct_key = random.choice(keys)
    print(correct_key, end='\r')
    with keyboard.Events as events:
        event = events.get(1)
        if event is None:
            print('You missed the key')
        elif event.key == correct_key:
            print('You pressed the correct key')
        else:
            print('You pressed the wrong key')


   
