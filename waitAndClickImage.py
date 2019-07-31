from waitImage import *


def waitAndClickImage(pathImage, addX = 0, addY = 0, mouseButton = 'left'):
    
    # Wait until pathImage is on screen, click on center of image
    # and return coodinates of pathImage.
    
    x,y = waitImage(pathImage)
    pyautogui.click(x = x + addX, y = y + addY, button = mouseButton)
    
    return x,y