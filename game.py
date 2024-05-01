from pynput import keyboard
import datetime
import time
import random
fishType = ['karas', 'kapr', 'pstruh', 'štika', 'sumec', 'žralok', 'velryba']
fishID = {'karas': 1, 'kapr': 2, 'pstruh': 3, 'štika': 4, 'sumec': 5, 'žralok': 6, 'velryba': 7}
fishValue = {'karas': 1, 'kapr': 3, 'pstruh': 5, 'štika': 10, 'sumec': 20, 'žralok': 50, 'velryba': 100}
fishQuality = ['malý', 'střední', 'velký', 'obrovský']
fishcaughtNum = 0
fishcaughtValue = 0
fishcaughtNames = []

key_pressed = False
gameStart = True

keys = ['q', 'w', 'e', 'r', 't', 'y', 'z']




class fishCatch:
    @staticmethod
    def catchFish(time, amount):
        for i in range(0, amount):
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
                    print('You pressed the wrong key', end='')
                    return False
   



while gameStart:
    time.sleep(2)
    fishChoose = random.randint(0, 1000)
    if fishChoose < 400:
        fishCaught = fishCaught.catchFish(2, 5)
        if fishCaught:
            print('Chytl jsi karase!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['karas']
            fishcaughtNames.append('karas')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >= 400 and fishChoose < 600:
        fishCaught = fishCaught.catchFish(1, 5)
        if fishCaught:
            print('Chytl jsi kapra!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['kapr']
            fishcaughtNames.append('kapr')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >=600 and fishChoose < 700:
        fishCaught = fishCaught.catchFish(0.5, 10)
        if fishCaught:
            print('Chytl jsi pstruha!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['pstruh']
            fishcaughtNames.append('pstruh')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 700 and fishChoose < 750:
        fishCaught = fishCaught.catchFish(0.3, 10)
        if fishCaught:
            print('Chytl jsi štiku!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['štika']
            fishcaughtNames.append('štika')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 750 and fishChoose < 775:
        fishCaught = fishCaught.catchFish(0.2, 15)
        if fishCaught:
            print('Chytl jsi sumce!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['sumec']
            fishcaughtNames.append('sumec')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >= 775 and fishChoose < 785:
        fishCaught = fishCaught.catchFish(0.1, 15)
        if fishCaught:
            print('Chytl jsi žraloka!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['žralok']
            fishcaughtNames.append('žralok')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 785 and fishChoose < 790:
        fishCaught = fishCaught.catchFish(0.05, 10)
        if fishCaught:
            print('Chytl jsi velrybu!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['velryba']
            fishcaughtNames.append('velryba')
        else:
            print('Nechytil jsi rybu')
    
    
    
    print("\033[H\033[J", end="")


   
