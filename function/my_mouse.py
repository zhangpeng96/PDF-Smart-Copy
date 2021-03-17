from pynput.mouse import Listener
from pynput import keyboard
from types import SimpleNamespace
import time
import pyperclip3
from english_paragraph import EnglishParagraph

flag = SimpleNamespace(time=0)

kb = keyboard.Controller()


def on_click(x, y, button, pressed):
    if pressed:
        flag.time = time.time()
    else:
        flag.time = time.time() - flag.time
        if flag.time > 1.25:
            kb.press(keyboard.Key.ctrl)
            kb.press('c')
            kb.release(keyboard.Key.ctrl)
            kb.release('c')
            time.sleep(0.4)
            # with kb.pressed(keyboard.Key.ctrl, 'c'):
            #     print('ctrl+c')
            clipboard = pyperclip3.paste()
            print('raw >> ', clipboard)
            data = EnglishParagraph(clipboard)
            print('fit >> ', data)
            pyperclip3.copy(data)


with Listener(on_click=on_click) as listener:
    listener.join()
