import pyautogui

pyautogui.FAILSAFE = True

# screenshot = pyautogui.screenshot('screenshot.png')
choice = input("What would you like to do?")

if choice == "craft button":
    pyautogui.PAUSE = 2.5
    x, y = pyautogui.locateCenterOnScreen('craftingButton.png')
    for i in range(100):
        pyautogui.mouseDown(button='left', x=x, y=y)
        # pyautogui.alert(text='Stop Holding?', title='', button='OK')
        pyautogui.mouseUp()
        print(i)

if choice == "aimbot":
    pyautogui.PAUSE = 0.3
    for i in range(1000):
        pyautogui.alert()
        x, y = pyautogui.locateCenterOnScreen('enemey.png')
        if (pyautogui.locateCenterOnScreen('enemey.png') is not None):
            pyautogui.click(x=x, y=y)