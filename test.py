from pynput import keyboard

def on_press(key):
    try:
        print('Key {0} pressed.'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed.'.format(key))

def on_release(key):
    print('Key {0} released.'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Create a listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the script running
while listener.is_alive():
    pass