from platform import python_branch
import pyautogui

#commands for mouse
# mouse-d = mouse button down (hold)
# mouse-c = mouse click



def main():
    command = input("What would you like to do?");
    command = str(command);
    if command == "mouse-d" :
        x = input("Press 'x' when ready to start and press is ");
        if x == "x":
            pyautogui.mouseDown(button='left');
            x = input("Press 'x' to stop");
            if x == "x":
                pyautogui.mouseUp(button='left')
    elif command == "mouse-c":
        x = input("Press 'x' when ready to start and press again to stop ");
        if x == "x":
            i = 0
            while i < 20:
                pyautogui.click(button='left')
                i = i+1



main();