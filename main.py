import pyautogui # pip install pyautogui
import time

a = int(input('Please enter number of entries'))

if __name__ == "__main__":
    print('Hot Key process has just begins, \n Just open tally software until 5 seconds passed')
    time.sleep(5)
    for i in range(0,a):
        pyautogui.keyDown('enter')
        pyautogui.keyDown('f3')
        pyautogui.keyDown('up')
        pyautogui.keyDown('enter')
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('alt', 'r')
        time.sleep(1)

