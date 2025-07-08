import pyautogui
import time

# Give time to manually open WhatsApp Desktop
print("Open WhatsApp Desktop and wait...")
time.sleep(5)

# Click on the search bar (you might need to adjust coordinates)
pyautogui.click(x=200, y=100)  # Change these coordinates to match the search bar
pyautogui.write('Yogesh')
time.sleep(1)

# Press Enter to open chat
pyautogui.press('enter')
time.sleep(1)

# Type and send the message
pyautogui.write('Hi')
pyautogui.press('enter')
