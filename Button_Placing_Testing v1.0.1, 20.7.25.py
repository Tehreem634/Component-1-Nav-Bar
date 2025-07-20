'''
COMPONENT #1
**Testing buttons for potential placements/figuring out**

Name: Tehreem Fatima
Date: 20/07/2025 - 20/07/2025
Purpose: Create a working navigation bar on the bottom of my app frame. 
'''
# Importing libraries
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
page4 = Frame(win)
page5 = Frame(win)
page6 = Frame(win)

# Putting pages into containers
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
page6.grid(row=0, column=0, sticky="nsew")

# Displaying the pages
label1 = tk.Label(page1, text="I am page 1", font=style1)
label1.pack(pady=20)

label2 = tk.Label(page2, text="I am page 2", font=style1)
label2.pack(pady=20)

label3 = tk.Label(page3, text="I am page 3", font=style1)
label3.pack(pady=20)

label4 = tk.Label(page4, text="I am page 4", font=style1)
label4.pack(pady=20)

label5 = tk.Label(page5, text="I am page 5", font=style1)
label5.pack(pady=20)

label6 = tk.Label(page6, text="I am page 6", font=style1)
label6.pack(pady=20)

# Displaying buttons on page 1 that lead to their own frames
button1 = Button(page1, text="Show Page 1", command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=40, pady=150)

# Page 1 (Frame 1) will show on the initial window when run
page1.tkraise()

# Specifications/Dimensions
win.title("Muslim Helper NZ")
win.geometry("500x400")
win.mainloop()
