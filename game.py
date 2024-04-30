from pynput import keyboard
import datetime
key_pressed = False

class keyLogger:
    @staticmethod
    def on_press(key):
        global start_time
        global key_pressed
        if key_pressed == False:
            start_time = datetime.datetime.now()
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
        end_time = datetime.datetime.now()
        key_pressed = False
        print('Key pressed for: ', end_time - start_time)
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

# Collect events until released
with keyboard.Listener(
        on_press=keyLogger.on_press,
        on_release=keyLogger.on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=keyLogger.on_press,
    on_release=keyLogger.on_release,)
