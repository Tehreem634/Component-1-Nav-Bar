"""
COMPONENT #1
[Navigation Bar]

Name: Tehreem Fatima
Date: 16/07/2025 - 17/07/2025
Purpose: Create a working navigation bar on the bottom of my app frame. 
"""

# Import libraries needed 
import tkinter as tk
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
    
# Creating main window
# Using variables
win = tk.Tk()

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

# Button image
button_image_1 = ImageTk.PhotoImage(Image.open("home_page_icon.png").resize((100,100)))
button_image_2 = ImageTk.PhotoImage(Image.open("prayers_page_icon.png").resize((100,100)))
button_image_3 = ImageTk.PhotoImage(Image.open("qibla_page_icon.png").resize((100,100)))
button_image_4 = ImageTk.PhotoImage(Image.open("community_page_icon.png").resize((100,100)))
button_image_5 = ImageTk.PhotoImage(Image.open("masjid_page_icon.png").resize((100,100)))
button_image_6 = ImageTk.PhotoImage(Image.open("settings_page_icon.png").resize((100,100)))

# All pages will be in the main container of win
page1 = Frame(win)
page2 = Frame(win)
page3 = Frame(win)
page4 = Frame(win)
page5 = Frame(win)
page6 = Frame(win)
page1.config(bg="#070B34")
page2.config(bg="#070B34")
page3.config(bg="#070B34")
page4.config(bg="#070B34")
page5.config(bg="#070B34")
page6.config(bg="#070B34")

# Putting pages into containers
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
page6.grid(row=0, column=0, sticky="nsew")

# Displaying the pages
label1 = tk.Label(page1, text="Home Page", font=style1, bg="#070B34", fg="white")
label1.pack(pady=20)

label2 = tk.Label(page2, text="Prayers Page", font=style1, bg="#070B34", fg="white")
label2.pack(pady=20)

label3 = tk.Label(page3, text="Qibla Finder Page", font=style1, bg="#070B34", fg="white")
label3.pack(pady=20)

label4 = tk.Label(page4, text="Community Page", font=style1, bg="#070B34", fg="white")
label4.pack(pady=20)

label5 = tk.Label(page5, text="Masjid locator Page", font=style1, bg="#070B34", fg="white")
label5.pack(pady=20)

label6 = tk.Label(page6, text="Settings Page", font=style1, bg="#070B34", fg="white")
label6.pack(pady=20)

# Displaying buttons on page 1 that lead to their own frames
button1 = Button(page1, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page1, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page1, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page1, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page1, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page1, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 2
button1 = Button(page2, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page2, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page2, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page2, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page2, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page2, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 3
button1 = Button(page3, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page3, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page3, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page3, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page3, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page3, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 4
button1 = Button(page4, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page4, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page4, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page4, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page4, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page4, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 5
button1 = Button(page5, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page5, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page5, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page5, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page5, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page5, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 6
button1 = Button(page6, image=button_image_1, command=lambda: page1.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button1.pack(side=tk.LEFT, padx=0, pady=560)

button2 = Button(page6, image=button_image_2, command=lambda: page2.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page6, image=button_image_3, command=lambda: page3.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page6, image=button_image_4, command=lambda: page4.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page6, image=button_image_5, command=lambda: page5.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page6, image=button_image_6, command=lambda: page6.tkraise(), font=style2, bg="#070B34", activebackground="#111545")
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Page 1 (Frame 1) will show on the initial window when run
page1.tkraise()

# Load the image using PhotoImage
icon_image = tk.PhotoImage(file="icon.png")
# Set the icon
win.iconphoto(False, icon_image)

# Specifications/Dimensions
win.title("Muslim Helper NZ")
win.geometry("635x750")
win.configure(bg="#070B34")
win.mainloop()
