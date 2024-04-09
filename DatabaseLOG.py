# Database Login project
#ITM 350


import tkinter as tk
from tkinter import font as tkFont  # Import tkinter font module to customize fonts

from tkinter import messagebox
import mysql.connector

window =tk.Tk()


class Mainwindow:
    def __init__(self, window):
        # Create the window
        self.window = window
        self.window.geometry("400x500")  # Increased window size for a more spacious layout

        # Create frame inside window for the login interface, with increased size for a more appealing look
        self.framelog = tk.Frame(window, background="light gray")  # Changed background color for a splash of color
        self.framelog.place(relx=0.5, rely=0.5, anchor='center', width=800, height=600)
        self.framelog.pack_propagate(False)  # Prevent frame from shrinking to fit its content

        # Define fonts
        titleFont = tkFont.Font(family="Arial", size=20, weight="bold")
        inputFont = tkFont.Font(family="Arial", size=14)
        buttonFont = tkFont.Font(family="Arial", size=12, weight="bold")
        linkFont = tkFont.Font(family="Arial", size=12, underline=True)

        # "Log in" title
        self.login_title = tk.Label(self.framelog, text="Log in", font=titleFont, bg="light gray")
        self.login_title.pack(pady=(20, 30))

        # Username label and entry, with increased font size and padding for better organization
        self.username_label = tk.Label(self.framelog, text="Username", font=inputFont, bg="light gray")
        self.username_label.pack(pady=(0, 10))

        self.username_entry = tk.Entry(self.framelog, font=inputFont)
        self.username_entry.pack(pady=(0, 20))

        # Password label, entry, and forget password link, with increased font size and padding
        self.password_label = tk.Label(self.framelog, text="Password", font=inputFont, bg="light gray")
        self.password_label.pack(pady=(0, 10))

        self.password_entry = tk.Entry(self.framelog, show="*", font=inputFont)
        self.password_entry.pack(pady=(0, 10))

        self.forget_password = tk.Label(self.framelog, text="Forget password?", font=linkFont, bg="light gray", fg="blue")
        self.forget_password.pack(pady=(0, 30))

        # Change 'add_student' method in logon button to 'self.logon'
        self.logon_button = tk.Button(self.framelog, text="Logon", font=buttonFont, bg="blue", fg="white", padx=10, pady=5, command=self.logon)
        self.logon_button.pack(pady=20)
        # Intriguing sign-up option
        self.signup_text = tk.Label(self.framelog, text="Don't have an account?", font=inputFont, bg="light gray")
        self.signup_text.pack(pady=(30, 10))
        # Add command for sign_up method to the signup_button
        self.signup_button = tk.Button(self.framelog, text="Sign Up", font=buttonFont, bg="green", fg="white", padx=10, pady=5, command=self.sign_up)
        self.signup_button.pack()

    def logon(self):
        # Create a new window for logon confirmation
        access_window = tk.Toplevel(self.window)
        access_window.title("Access Granted")
        access_window.geometry("300x200")  # Set the size of the new window

        # Add a label to the access window
        label = tk.Label(access_window, text="You have access")
        label.pack(pady=20)

        # Add a close button to the access window
        close_button = tk.Button(access_window, text="Close", command=access_window.destroy)
        close_button.pack(pady=10)

    def sign_up(self):
        # Create a new window for signing up
        signup_window = tk.Toplevel(self.window)
        signup_window.title("Sign Up")
        signup_window.geometry("300x200")  # Set the size of the new window

        # Username entry
        username_label = tk.Label(signup_window, text="Create Username:")
        username_label.pack(pady=(20, 5))
        username_entry = tk.Entry(signup_window)
        username_entry.pack(pady=(0, 20))

        # Password entry
        password_label = tk.Label(signup_window, text="Create Password:")
        password_label.pack(pady=(0, 5))
        password_entry = tk.Entry(signup_window, show="*")
        password_entry.pack(pady=(0, 20))

        # Add a submit button to the sign-up window
        submit_button = tk.Button(signup_window, text="Submit", command=lambda: self.create_account(username_entry.get(), password_entry.get()))
        submit_button.pack(pady=10)

    def create_account(self, username, password):
        # Placeholder method for account creation logic
        print("Creating account:", username, password)
        # Add logic to create an account with the given username and password

# Create the main application window
root = tk.Tk()
app = Mainwindow(root)

# Start the Tkinter event loop
root.mainloop()
