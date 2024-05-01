from pynput import keyboard
import datetime
import time
import random
fishType = ['karas', 'kapr', 'pstruh', 'štika', 'sumec', 'žralok', 'velryba']
fishID = {'karas': 1, 'kapr': 2, 'pstruh': 3, 'štika': 4, 'sumec': 5, 'žralok': 6, 'velryba': 7}
fishValue = {'karas': 1, 'kapr': 3, 'pstruh': 5, 'štika': 10, 'sumec': 20, 'žralok': 50, 'velryba': 100}
fishQuality = ['malý', 'střední', 'velký', 'obrovský']

key_pressed = False
gameStart = True

keys = ['q', 'w', 'e', 'r', 't', 'y', 'z']




class keyLogger:
    @staticmethod
    def on_press(key):
        global start_time
        global key_pressed
        if key_pressed == False:
            start_time = datetime.datetime.now().microsecond
            key_pressed = True
        else:
            key_pressed = True

    def on_release(key):
        global end_time
        global key_pressed
        end_time = datetime.datetime.now().microsecond
        key_pressed = False
        if key == keyboard.Key.esc:
            # Stop listener
            return False
press = keyLogger.on_press
release = keyLogger.on_release

listener = keyboard.Listener(press, release)
listener.start()


while gameStart:
    time.sleep(2)
    fishChoose = random.randint()
    correct_key = random.choice(keys)
    print(correct_key, end='\r')
    with keyboard.Events() as events:
        event = events.get(5)
        pressed_key = event.key.char
        if event is None:
            print('You missed the key', end='\r')
        elif pressed_key == correct_key:
            print('You pressed the correct key', end='\r')
        else:
            print('You pressed the wrong key', end='')
            print(pressed_key, end='\r')
        print("\033[H\033[J", end="")


   
