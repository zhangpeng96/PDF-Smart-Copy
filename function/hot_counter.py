from pynput import keyboard
import pyperclip3

cont = keyboard.Controller()

counter_start = 42
counter_end = 50

counters = [
    map(lambda i: '[^{}]'.format(i), range(counter_start, counter_end+1)),
    map(lambda i: '[^{}]: '.format(i), range(counter_start, counter_end+1)),
]


def key_paste():
    with cont.pressed(keyboard.Key.ctrl):
        cont.press('v')
        cont.release('v')


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key == keyboard.Key.ctrl_r:
        try:
            text = next(counters[0])
            pyperclip3.copy(text)
            key_paste()
            print('#C1 √: {}'.format(text))
        except Exception as e:
            print('#C1 ×')
            print(e)
    elif key == keyboard.Key.shift_r:
        try:
            text = next(counters[1])
            pyperclip3.copy(text)
            key_paste()
            print('#C2 √: {}'.format(text))
        except Exception as e:
            print('#C2 ×')
            print(e)



# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
# on_press=on_press, 
# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()