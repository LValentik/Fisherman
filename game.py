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




class fishCatch:
    @staticmethod
    def catchFish(time):
        with keyboard.Events() as events:
            event = events.get(time)
            pressed_key = event.key.char
            correct_key = random.choice(keys)
            if event is None:
                print('You missed the key', end='\r')
                return False
            elif pressed_key == correct_key:
                print('You pressed the correct key', end='\r')
            else:
                print('You pressed the wrong key', end='')S
                return False
        
   


while gameStart:
    time.sleep(2)
    fishChoose = random.randint(0, 1000)
    

    
    
    
    
    print("\033[H\033[J", end="")


   
