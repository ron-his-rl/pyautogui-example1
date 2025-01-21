import pyautogui
import os
import pygetwindow

def activate_window(title):
    try:
        window = pygetwindow.getWindowsWithTitle(title)[0]
        window.activate()
    except IndexError:
        print("Window not found:", title)

#os.startfile("outlook")
activate_window("Inbox - ron.hiscock@rlglobal.com - Outlook")
pyautogui.hotkey('ctrl', 'n')
print(pyautogui.position())
pyautogui.typewrite('elijah.sprung@rlglobal.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('Automated email:')
pyautogui.press('tab')
pyautogui.typewrite('This is an automaed email, please do not reply.')
pyautogui.hotkey('ctrl', 'enter')