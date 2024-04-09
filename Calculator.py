#Burke Sullivan

# ITM 360

# LAB 2: Calculator

import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.configure(background='black')  # Set the background of the root window to black
root.geometry("300x400")  # Adjust size as needed

# Display Frame
display_frame = tk.Frame(root, background='black')
display_frame.pack(pady=10)

display = tk.Entry(display_frame, font=('Helvetica', 24), borderwidth=5, relief="sunken", justify="right", background="black", foreground="white")
display.pack(padx=10, pady=10)

# Variables to store the first operand, operator, and state
first_operand = None
operator = None
is_operation_selected = False

# Define the functions (append_to_display, set_operation, calculate, clear_display, negate, percentage)
# Functions should remain the same as in your original code, so they're omitted here for brevity

# Buttons Frame
buttons_frame = tk.Frame(root, background='black')
buttons_frame.pack(expand=True, fill="both")

# Configure button styles with ttk.Style
style = ttk.Style()
style.theme_use('clam')  # Using a theme that allows for more customization

# Configure the style for regular buttons
style.configure("TButton", font=('Helvetica', 14), foreground="white", background="black", borderwidth=1)
style.map("TButton",
          foreground=[('active', 'white')],
          background=[('active', 'black')])

# Configure the style for operation buttons
style.configure("Operation.TButton", font=('Helvetica', 14), foreground="white", background="orange", borderwidth=1)
style.map("Operation.TButton",
          foreground=[('active', 'white')],
          background=[('active', 'orange')])

# Create buttons list for display with button texts, their grid positions, commands, and optional styles
buttons = [
    ('7', 1, 0, '7'), ('8', 1, 1, '8'), ('9', 1, 2, '9'), ('/', 1, 3, 'set_operation', "Operation.TButton"),
    ('4', 2, 0, '4'), ('5', 2, 1, '5'), ('6', 2, 2, '6'), ('*', 2, 3, 'set_operation', "Operation.TButton"),
    ('1', 3, 0, '1'), ('2', 3, 1, '2'), ('3', 3, 2, '3'), ('-', 3, 3, 'set_operation', "Operation.TButton"),
    ('0', 4, 0, '0'), ('.', 4, 1, '.'), ('+/-', 4, 2, 'negate'), ('+', 4, 3, 'set_operation', "Operation.TButton"),
    ('%', 5, 0, 'percentage'), ('C', 5, 1, 'clear_display'), ('=', 5, 2, 'calculate', "Operation.TButton", 2)
]

# Configure button grid
for text, row, col, command, *options in buttons:
    cmd = globals()[command] if callable(globals()[command]) else lambda cmd=command: append_to_display(cmd)
    style = options[0] if options else "TButton"
    col_span = options[1] if len(options) > 1 else 1
    btn = ttk.Button(buttons_frame, text=text, command=cmd, style=style)
    btn.grid(row=row, column=col, columnspan=col_span, sticky="nsew", padx=5, pady=5)
    buttons_frame.grid_columnconfigure(col, weight=1)

# Make rows and columns in the grid expand equally
for i in range(6):
    buttons_frame.grid_rowconfigure(i, weight=1)

# Run the program
root.mainloop()
