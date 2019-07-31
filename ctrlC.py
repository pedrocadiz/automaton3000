import win32clipboard
import pyautogui

def ctrlC():

    # Copy the content of the clipboard, after we delete
    # the clipboard
    
    pyautogui.hotkey('ctrl', 'c')
    
    win32clipboard.OpenClipboard()
    stringFromClipboard = win32clipboard.GetClipboardData()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    
    return stringFromClipboard