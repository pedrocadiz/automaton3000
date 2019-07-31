import pyautogui
import os

def waitImage(pathImage):

    # Wait until pathImage is on screen, return center coodinates of pathImage
    
    flag = 0
    while(flag == 0):
        try:
            x,y = pyautogui.locateCenterOnScreen(pathImage, confidence=0.9)
            flag = 1
        except TypeError:
            print(os.path.basename(pathImage) + " is not on screen")
            
    return x,y