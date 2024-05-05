from pynput import keyboard
import datetime
import time
import random
import psycopg
import getpass


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





class DataWork:
    @staticmethod

    def LogRes():
        global username
        global conn
        global cur
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        try:
            conn = psycopg.connect(host='localhost', dbname='fishgame', port=5432, user='postgres', password='VaLeNtIk2007.')
            cur = conn.cursor()

            # Check if the user exists
            cur.execute('SELECT * FROM accounts.acc WHERE "user" = %s AND "pass" = %s;', (username, password))
            if cur.fetchone() is not None:
                print("Login successful.")
                return True
            else:
                # If the user doesn't exist, create a new account
                cur.execute('INSERT INTO accounts.acc ("user", "pass", "value") VALUES (%s, %s, 0);', (username, password))
                conn.commit()
                print("Registered successfully.")
                return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        finally:
            cur.close()
            conn.close()
    
    def InvUpload():
        try:
            cur.execute()
        except Exception as er:
            print(f"An error occured: {er}")
            return False
        finally:

class fishCatch:
    @staticmethod
    def catchFish(time, amount):
        for i in range(0, amount):
            with keyboard.Events() as events:
                correct_key = random.choice(keys)
                print(correct_key, end='\r')
                event = events.get(time)
                if event is None:
                    print('You missed the key', end='\r')
                    return False
                
                pressed_key = event.key.char
                print(pressed_key, end='')
                time.sleep(2)
                if pressed_key == correct_key:
                    print('You pressed the correct key', end='\r')
                else:
                    print('You pressed the wrong key', end='')
                    return False
                print("\033[H\033[J", end="")
        return True
   
signin = DataWork.LogRes()

while signin:
   
    time.sleep(2)
    fishChoose = random.randint(0, 1000)
    if fishChoose < 400:
        fishCaught = fishCatch.catchFish(3, 5)
        if fishCaught:
            print('Chytl jsi karase!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['karas']
            fishcaughtNames.append('karas')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >= 400 and fishChoose < 600:
        fishCaught = fishCatch.catchFish(2, 5)
        if fishCaught:
            print('Chytl jsi kapra!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['kapr']
            fishcaughtNames.append('kapr')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >=600 and fishChoose < 700:
        fishCaught = fishCatch.catchFish(2, 10)
        if fishCaught:
            print('Chytl jsi pstruha!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['pstruh']
            fishcaughtNames.append('pstruh')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 700 and fishChoose < 750:
        fishCaught = fishCatch.catchFish(1, 10)
        if fishCaught:
            print('Chytl jsi štiku!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['štika']
            fishcaughtNames.append('štika')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 750 and fishChoose < 775:
        fishCaught = fishCatch.catchFish(1, 15)
        if fishCaught:
            print('Chytl jsi sumce!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['sumec']
            fishcaughtNames.append('sumec')
        else:
            print('Nechytil jsi rybu')
    
    if fishChoose >= 775 and fishChoose < 785:
        fishCaught = fishCatch.catchFish(0.8, 15)
        if fishCaught:
            print('Chytl jsi žraloka!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['žralok']
            fishcaughtNames.append('žralok')
        else:
            print('Nechytil jsi rybu')
            
    if fishChoose >= 785 and fishChoose < 790:
        fishCaught = fishCatch.catchFish(0.6, 10)
        if fishCaught:
            print('Chytl jsi velrybu!')
            fishcaughtNum =+ 1
            fishcaughtValue =+ fishValue['velryba']
            fishcaughtNames.append('velryba')
        else:
            print('Nechytil jsi rybu')
    
    
    
    print("\033[H\033[J", end="")


   
