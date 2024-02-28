from tkinter import *
from Tamagotchi import Pet

import tkinter as tk
from tkinter import Frame, Label
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Image Frame GUI")

# Set the size of the window
root.geometry("600x400")

# Create a frame in the middle of the window
frame = Frame(root,width=300, height=200, bg='grey')
frame.pack(expand=True, fill='both')

# Load an image (replace 'placeholder.png' with your image file)
image = Image.open("kittyboo.webp")
image = image.resize((250, 150))  # Resize image to fit the frame
  # Resize image to fit the frame
photo = ImageTk.PhotoImage(image)

# Create a label to display the image and add it to the frame
label = Label(frame, image=photo)
label.image = photo  # Keep a reference to the image
label.pack(padx=10, pady=10)

# Creating an entry for user and button to teach
def teach_sound():
    new_sound = entry.get()
    if new_sound:
        Pet.teach(new_sound)
        entry.delete(0,"end")
entry = Entry(root)
entry.pack()

my_button = Button(root, text = "Teach", command=teach_sound())
my_button.pack()

# Start the GUI event loop
root.mainloop()
