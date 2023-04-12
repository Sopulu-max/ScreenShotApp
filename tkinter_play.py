"""
This file is meant to be a playground for the tkinter python module
Tkinter is the standard GUI library for Python.
Feel free to get your hands dirty with the module functions and methods
while you try to learn and understand whaht each one does
read more here
https://docs.python.org/3/library/tkinter.html
"""

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Playground")

window.mainloop()
# mainloop() is simply a method in the main window
# that executes what we wish to execute in an 
# application (lets Tkinter to start running the application). 
# As the name implies it will loop forever until the user 
# exits the window or waits for any events from the user. 
# The mainloop automatically receives events from the 
# window system and deliver them to the application widgets. 
# This gets quit when we click on the close button of the title bar. 
# So, any code after this mainloop() method will not run.