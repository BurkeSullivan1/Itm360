import tkinter as tk
from tkinter import ttk

import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.configure(background='black')
root.geometry("300x400") # set size of calculator

# Display Frame
display_frame = tk.Frame(root, background='black')
display_frame.pack(pady=10)

# Frame of result box
display = tk.Entry(display_frame, font=('Helvetica', 24), borderwidth=5, relief="sunken", justify="right", background="black", foreground="white")
display.pack(padx=10, pady=10)

# Variables to store the first operand, operator, and state
first_operand = None
operator = None
is_operation_selected = False

# Function to append characters to the display
def append_to_display(text):
    global is_operation_selected #global var
    if is_operation_selected:  # if true - selection
        display.delete(0, tk.END)  # Clears display
        is_operation_selected = False
    display.insert(tk.END, text) #Insert value

# Function to set the operation
def set_operation(op):
    global first_operand, operator, is_operation_selected
    if display.get() != "":  # Only set operation if there is a number
        first_operand = float(display.get()) # grabs value
        operator = op
        is_operation_selected = True

# Function to calculate and display the result
def calculate():
    global first_operand, operator
    if display.get() != "" and first_operand is not None:
        second_operand = float(display.get())
        result = None
        if operator == "+":
            result = first_operand + second_operand # add togeather
        elif operator == "-":
            result = first_operand - second_operand # subtract
        elif operator == "*":
            result = first_operand * second_operand #multiply
        elif operator == "/":
            result = first_operand / second_operand if second_operand != 0 else "Error" #divide and check if value is not 0

        display.delete(0, tk.END) # delete valyues
        display.insert(0, str(result))
        first_operand = None  # Reset for new calculations

# Function to clear the display and reset variables
def clear_display():
    global first_operand, operator, is_operation_selected
    display.delete(0, tk.END)  # clears display
    first_operand = None
    operator = None
    is_operation_selected = False

# Function for negation
def negate():
    current_value = display.get()
    if current_value:
        new_value = -1 * float(current_value)
        display.delete(0, tk.END)
        display.insert(0, str(new_value))

# Function for percentage
def percentage():
    current_value = display.get()
    if current_value:
        new_value = float(current_value) / 100
        display.delete(0, tk.END)
        display.insert(0, str(new_value))

# Buttons Frame
buttons_frame = tk.Frame(root, background='black')
buttons_frame.pack(expand=True, fill="both")

# Button details: text, row, col, command,
buttons = [
    ('7', 0, 0, '7'), ('8', 0, 1, '8'), ('9', 0, 2, '9'), ('/', 0, 3, '/'),
    ('4', 1, 0, '4'), ('5', 1, 1, '5'), ('6', 1, 2, '6'), ('*', 1, 3, '*'),
    ('1', 2, 0, '1'), ('2', 2, 1, '2'), ('3', 2, 2, '3'), ('-', 2, 3, '-'),
    ('0', 3, 0, '0'), ('.', 3, 1, '.'), ('+/-', 3, 2, negate), ('+', 3, 3, '+'),
    ('%', 4, 0, percentage), ('C', 4, 1, clear_display), ('=', 4, 2, calculate, 2)  # Span '=' button over 2 columns
]

# Create and place buttons in the grid using for loop
for text, row, col, command, *span in buttons:
    action = command if callable(command) else lambda cmd=command: set_operation(cmd) if cmd in ['+', '-', '*', '/'] else append_to_display(cmd)
    btn = tk.Button(buttons_frame, text=text, command=action, bg='black', fg='white', font=('Helvetica', 14))
    col_span = span[0] if span else 1
    btn.grid(row=row, column=col, columnspan=col_span, sticky="nsew", padx=5, pady=5)

# Configure grid to expand buttons equally
for i in range(5):  # 5 rows
    buttons_frame.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    buttons_frame.grid_columnconfigure(j, weight=1)

root.mainloop()
