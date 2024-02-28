import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

# Function to be called when the button is clicked
def on_button_click():
    print("Button clicked!")
def program_lang():
    tk.Label(top_frame, text= "intresting topics").pack()
def python_more()
    tk.Label(top_frame,text="desirable skillsset").pack()
# Create a new Tkinter application
app = tk.Tk()

# Set the title of the window
app.title("My GUI")

# create two frames
top_frame = tk.Frame(app,borderwidth=1 , highlightbackground='black').pack()
bottom_frame =tk.Frame(app,highlightthickness=1).pack()
# Set the size of the window
app.geometry("400x300")
messagebox.showinfo("Itm 360", "Would you like to take Itm 360?")
# Create a Button widget
# 'bg' sets the background color, 'fg' sets the text color
button = tk.Button(top_frame, text="Yes", bg="green", fg="white", command=on_button_click).place(x = 100, y = 100)
button_2 = tk.Button(top_frame,text="no",bg = "red", fg = "white").place(x=200, y=100)
# multiple ways to gemoetry allocate things GUI - pack(), Place(), Grid ()
btn1 = tk.Button(top_frame, text="Pros of taking itm 360",fg = "green",command = program_lang)
button_check = tk.Checkbutton(app, text = "python?").place(x=300, y=200)

# Position the button in the window
# The pack method is one of Tkinter's geometry managers
#button.pack(pady=20)  # 'pady' adds some vertical padding around the button

# Start the GUI event loop
app.mainloop()