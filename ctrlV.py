import win32clipboard
import pyautogui

def ctrlV(stringToCopy):

    # Put stringToCopy on the clipboard and push
    # ctrl+v, after we erase tthe clipboard

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(stringToCopy)
    win32clipboard.CloseClipboard()
    
    pyautogui.hotkey('ctrl', 'v') 
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()