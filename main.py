"""building a Screenshot app using pyautogui and pilow"""
import pyautogui as ptg
import tkinter as tk
from tkinter.filedialog import *

# a function to take screenshot
def take_screenshot():
    screenshot = ptg.screenshot()
    # use tkinter's asksaveasfilename function to ask user for a filepath to save
    save_path = asksaveasfilename(defaultextension=".png")
    # save the screenshot
    screenshot.save(save_path)


# create a tkinter parent window
window = tk.Tk()
# add title to be displayed at the top of the window
window.title("Screenshot Taker")

# create a tkinter button and bound the take screenshot function to it
button = tk.Button(window, text="Take Screenshot", command=take_screenshot)
button.pack()

# call window.mainloop()
window.mainloop()