import pyautogui
import time
import math
from datetime import datetime
import sys
pyautogui.FAILSAFE = False
max_hour = 19


def mouse_move():
    try:
        (x, y) = pyautogui.size()
        (X, Y) = pyautogui.position(x / 2, y / 2)
        R = min([x, y]) / 3

        while (True):
            now = datetime.now()
            hour = now.hour
            if hour >= max_hour:
                print(f'Break, hit max hour {format(datetime.now().time())}')
                break
            else:
                pyautogui.press('shift')
                pyautogui.moveTo(X + R, Y)
                for i in range(360):
                    if i % 6 == 0:
                        pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
                print(f'Movement made at {format(datetime.now().time())}')
                time.sleep(60)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    mouse_move()

