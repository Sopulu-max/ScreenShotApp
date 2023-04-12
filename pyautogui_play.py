"""
This file is meant to be a playground for the pyauotogui python library
Feel free to get your hands dirty with the library functions and methods
while you try to learn and understand whaht each one does
read more here 
https://pyautogui.readthedocs.io/en/latest/
"""
import pyautogui as gui

# Get the size of the primary monitor
screenWidth, screenHeight = gui.size()
print(screenWidth, screenHeight)

# Get the XY position of the mouse.
currentMouseX, currentMouseY = gui.position()
print(currentMouseX, currentMouseY)

# Move the mouse to XY coordinates.
# pyautogui.moveTo(100, 150)



gui.screenshot()