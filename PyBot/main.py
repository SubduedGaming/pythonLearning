import time
import pyautogui



def main():
    
    
    pyautogui.FAILSAFE = True
    
    
    #Countdown Timer
    print("Starting", end="")
    for i in range(1, 10):
        print(".", end="")
        time.sleep(1)
    
    #Actions
    pyautogui.moveTo(100, 100, duration=1)
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()