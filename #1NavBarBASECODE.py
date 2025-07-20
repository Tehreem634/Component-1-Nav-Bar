'''
COMPONENT #1
[Navigation Bar]
**TEMPLATE CODE**

Name: Tehreem Fatima
Date: 16/07/2025
Purpose:
        - CREATE BASE FOR NAV BAR CODE
        - Use a tutorial to learn how to link buttons to a page/frame.
        - This allows for potential *initial* navigation bar for my app;
          'Muslim Helper' (App name is currently temporary).
Tutorial/Skills learnt from: CodeWorked (youtube)

'''

import tkinter as tk
from tkinter import *
import tkinter.font

# Creating main window
# Using variables
win = tk.Tk() 

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

# All pages will be in the main container of win
page1 = Frame(win)
page2 = Frame(win)
page3 = Frame(win)

# Putting pages into containers
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")

# Displaying the pages
label1 = tk.Label(page1, text="I am page 1", font=style1)
label1.pack(pady=20)

label2 = tk.Label(page2, text="I am page 2", font=style1)
label2.pack(pady=30)

label3 = tk.Label(page3, text="I am page 3", font=style1)
label3.pack(pady=50)

# Displaying buttons on certain frames
# Leading to other frames
button1 = Button(page1, text="Show Page 2", command=lambda: page2.tkraise(), font=style2)
button1.pack() 

button2 = Button(page2, text="Show Page 1", command=lambda: page1.tkraise(), font=style2)
button3 = Button(page2, text="Show Page 3", command=lambda: page3.tkraise(), font=style2)

button2.pack()
button3.pack()

# Display page 3 with both other frame buttons
button4 = Button(page3, text="Show Page 1", command=lambda: page1.tkraise(), font=style2)
button5 = Button(page3, text="Show Page 2", command=lambda: page2.tkraise(), font=style2)

button4.pack()
button5.pack()

# Page 1 will show on the initial window when run
page1.tkraise()
# Specifications/Dimensions
win.title("Muslim Helper NZ")
win.geometry("500x400")
win.mainloop()
