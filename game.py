from pynput import keyboard
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
    
    def GameClose():
        try:
            
            fish_count = {}
            
            for fish in fishcaughtNames:
                if fish in fish_count:
                    fish_count[fish] += 1
                else:
                    fish_count[fish] = 1

            for fish, count in fish_count.items():
                cur.execute('INSERT INTO inventory.inv ("acc", "item", "value", "quantity") VALUES (%s, %s, %s, %s) ON CONFLICT ("acc", "item") DO UPDATE SET "quantity" = inventory.inv."quantity" + %s;', (username, fish, fish.fishValue, count, count))
                conn.commit()    
        
        
        
        except Exception as er:
            print(f"An error occured: {er}")
            return False
        finally:
            cur.close()
            conn.close()
            return True
    
    def InvShow():
        try:
            cur.execute('SELECT * FROM inventory.inv WHERE "acc" = %s;', (username))
            inventory = cur.fetchall()
            print("Your inventory:")
            for item in inventory:
                print(f"{item[1]}: {item[3]}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            cur.close()
            conn.close()
            return True
    
    def InvSell(fish_to_sell, quantity_to_sell):
        try:
        # Fetch the specific fish from the inventory
            cur.execute('SELECT * FROM inventory.inv WHERE "acc" = %s AND "item" = %s;', (username, fish_to_sell))
            fish = cur.fetchone()

            if fish is None:
                print(f"You don't have any {fish_to_sell}.")
                return False

            if fish[3] < quantity_to_sell:
                print(f"You don't have enough {fish_to_sell}. You only have {fish[3]}.")
                return False

            # Calculate the total value
            total_value = fish[2] * quantity_to_sell

            # Update the quantity of the fish in the inventory
            new_quantity = fish[3] - quantity_to_sell
            if new_quantity == 0:
                cur.execute('DELETE FROM inventory.inv WHERE "acc" = %s AND "item" = %s;', (username, fish_to_sell))
            else:
                cur.execute('UPDATE inventory.inv SET "quantity" = %s WHERE "acc" = %s AND "item" = %s;', (new_quantity, username, fish_to_sell))

            # Update the user's account value
            cur.execute('UPDATE accounts.acc SET "value" = "value" + %s WHERE "user" = %s;', (total_value, username))
            conn.commit()

            print(f"Sold {quantity_to_sell} {fish_to_sell} for {total_value} coins.")
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        finally:
            cur.close()
            conn.close()
    
    def StoreShow():
        try:
            cur.execute('SELECT * FROM store.items;')
            store = cur.fetchall()
            print("Store:")
            for item in store:
                print(f"{item[1]}: {item[2]} coins")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            cur.close()
            conn.close()
            return True
    def StoreBuy(item_to_buy, quantity_to_buy):
        try:
            cur.execute('SELECT * FROM store.items WHERE "item_name" = %s;', (item_to_buy,))
            item = cur.fetchone()

            if item is None:
                print(f"The item {item_to_buy} is not available in the store.")
                return False

            cur.execute('SELECT * FROM accounts.acc WHERE "user" = %s;', (username,))
            user = cur.fetchone()

            if user[3] < item[2] * quantity_to_buy:
                print(f"You don't have enough coins to buy {quantity_to_buy} {item_to_buy}. You need {item[2] * quantity_to_buy} coins.")
                return False

            if quantity_to_buy > item[3]:
                print(f"There are only {item[3]} {item_to_buy} available in the store.")
                return False

            cur.execute('UPDATE accounts.acc SET "value" = "value" - %s WHERE "user" = %s;', (item[2] * quantity_to_buy, username))
            cur.execute('INSERT INTO inventory.inv ("acc", "item", "value", "quantity") VALUES (%s, %s, %s, %s) ON CONFLICT ("acc", "item") DO UPDATE SET "quantity" = inventory.inv."quantity" + %s;', (username, item_to_buy, item[2], quantity_to_buy, quantity_to_buy))
            conn.commit()

            print(f"Bought {quantity_to_buy} {item_to_buy} for {item[2] * quantity_to_buy} coins.")

            # Remove the item from the store if the user bought all the items
            if quantity_to_buy >= item[3]:
                cur.execute('DELETE FROM store.items WHERE "item_name" = %s;', (item_to_buy,))
                conn.commit()

            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        finally:
            cur.close()
            conn.close()
            
            
            

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
    print("Welcome to the game!")
    print("Press '1' to start fishing")
    print("Press '2' to show your inventory")
    print("Press '3' to sell fish")
    print("Press '4' to show the store")
    print("Press '5' to buy from the store")
    print("Press '6' to exit the game")
    with keyboard.Events() as events:
        event = events.get()
        if event is not None:
            key = event.key
            if key == keyboard.Key.one:
                gameStart = True
            elif key == keyboard.Key.two:
                DataWork.InvShow()
            elif key == keyboard.Key.three:
                fish_to_sell = input("Enter the name of the fish you want to sell: ")
                quantity_to_sell = int(input("Enter the quantity you want to sell: "))
                DataWork.InvSell(fish_to_sell, quantity_to_sell)
            elif key == keyboard.Key.four:
                DataWork.StoreShow()
            elif key == keyboard.Key.five:
                item_to_buy = input("Enter the name of the item you want to buy: ")
                quantity_to_buy = int(input("Enter the quantity you want to buy: "))
                DataWork.StoreBuy(item_to_buy, quantity_to_buy)
            elif key == keyboard.Key.six:
                DataWork.GameClose()
                break
            else:
                print("Invalid key")
    
    
    while gameStart:
        time.sleep(random.uniform(1, 3))  # Randomized time between fish biting
        print("You've got a bite! Press the key to catch the fish!")
        time.sleep(1)
        fishChoose = random.randint(0, 790)
        if fishChoose < 400:
            fishCaught = fishCatch.catchFish(3, 5)
            if fishCaught:
                print('Chytl jsi karase!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['karas']
                fishcaughtNames.append('karas')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 400 and fishChoose < 600:
            fishCaught = fishCatch.catchFish(2, 5)
            if fishCaught:
                print('Chytl jsi kapra!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['kapr']
                fishcaughtNames.append('kapr')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 600 and fishChoose < 700:
            fishCaught = fishCatch.catchFish(2, 10)
            if fishCaught:
                print('Chytl jsi pstruha!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['pstruh']
                fishcaughtNames.append('pstruh')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 700 and fishChoose < 750:
            fishCaught = fishCatch.catchFish(1, 10)
            if fishCaught:
                print('Chytl jsi štiku!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['štika']
                fishcaughtNames.append('štika')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 750 and fishChoose < 775:
            fishCaught = fishCatch.catchFish(1, 15)
            if fishCaught:
                print('Chytl jsi sumce!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['sumec']
                fishcaughtNames.append('sumec')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 775 and fishChoose < 785:
            fishCaught = fishCatch.catchFish(0.8, 15)
            if fishCaught:
                print('Chytl jsi žraloka!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['žralok']
                fishcaughtNames.append('žralok')
            else:
                print('Nechytil jsi rybu')

        elif fishChoose >= 785 and fishChoose < 790:
            fishCaught = fishCatch.catchFish(0.6, 10)
            if fishCaught:
                print('Chytl jsi velrybu!')
                fishcaughtNum += 1
                fishcaughtValue += fishValue['velryba']
                fishcaughtNames.append('velryba')
            else:
                print('Nechytil jsi rybu')
    
    print("\033[H\033[J", end="")


   
