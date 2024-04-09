import tkinter as tk
from tkinter import ttk

# Initialize the main application window
root = tk.Tk()
root.title("Calculator")
root.configure(background='black')  # Set the background of the root window to black
root.geometry("300x400")  # Adjust size as needed

# Display frame for GUI
# Display Frame
display_frame = ttk.Frame(root, background='black')  # Set the background of the frame to black
display_frame.pack(pady=10)

display = tk.Entry(display_frame, font=('Helvetica', 24), borderwidth=5, relief="sunken", justify="right", background="black", foreground="white")
display.pack(padx=10, pady=10)

#Created variables for selections based off buttons pressed
# Variables to store the first operand, operator, and state
first_operand = None
operator = None
is_operation_selected = False

# Function to append characters to the display
# parameter is button clicked
def append_to_display(text):
    global is_operation_selected
    if is_operation_selected: #is something selected
        display.delete(0, tk.END) # clears display
        is_operation_selected = False
    display.insert(tk.END, text) # now inserts selected

# Function to set the operation
def set_operation(op):
    global first_operand, operator, is_operation_selected
    if not display.get() == "":  # only set operation if there is a number
        first_operand = float(display.get())  #turn str to float
        operator = op
        is_operation_selected = True

# Function to calculate and display the result
def calculate():
    global first_operand, operator  # reach global variables
    if not display.get() == "" and not first_operand is None:   #conditional
        second_operand = float(display.get())
        result = None
        if operator == "+":
            result = first_operand + second_operand
        elif operator == "-":
            result = first_operand - second_operand
        elif operator == "*":
            result = first_operand * second_operand
        elif operator == "/":
            result = first_operand / second_operand if second_operand != 0 else "Error"

        display.delete(0, tk.END) # delete
        display.insert(0, str(result)) #insert
        first_operand = None  # Reset the operand for new calculations

# Function to clear the display and reset variables
def clear_display():
    global first_operand, operator, is_operation_selected
    display.delete(0, tk.END)
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

# Function to clear the display and reset variables
def clear_display():
    global first_operand, operator, is_operation_selected
    display.delete(0, tk.END)
    first_operand = None
    operator = None
    is_operation_selected = False
# Buttons Frame
buttons_frame = tk.Frame(root, background='black')  # Set the background of the frame to black
buttons_frame.pack(expand=True, fill="both")
# Configure button styles
style = ttk.Style()
style.configure("TButton", background="black", foreground="white", font=('Helvetica', 14))
style.configure("Operation.TButton", background="orange", foreground="white", font=('Helvetica', 14))

# create buttons list for display
# button texts, their grid positions, and commands
buttons = [
    ('7', 1, 0, '7'), ('8', 1, 1, '8'), ('9', 1, 2, '9'), ('/', 1, 3, '/'),
    ('4', 2, 0, '4'), ('5', 2, 1, '5'), ('6', 2, 2, '6'), ('*', 2, 3, '*'),
    ('1', 3, 0, '1'), ('2', 3, 1, '2'), ('3', 3, 2, '3'), ('-', 3, 3, '-'),
    ('0', 4, 0, '0'), ('.', 4, 1, '.'), ('+/-', 4, 2, negate), ('+', 4, 3, '+'),
    ('%', 5, 0, percentage), ('C', 5, 1, clear_display), ('=', 5, 2, calculate, 2)  # Span '=' button over 2 columns
]

# Configure button grid

for text, row, col, command, *span in buttons:
    action = command if callable(command) else lambda cmd=command: set_operation(cmd) if cmd in ['+', '-', '*', '/'] else append_to_display(cmd)
    btn = ttk.Button(buttons_frame, text=text, command=action)
    col_span = span[0] if span else 1  # Set column span
    btn.grid(row=row, column=col, columnspan=col_span, sticky="nsew", padx=5, pady=5)
    buttons_frame.grid_columnconfigure(col, weight=1)


# Grid_rowconfigure is method for properties of rows in gird layout within a frame - vice versa with columns
# Make rows and columns in the grid expand equally
for i in range(6):  # 6 rows including the '=' button row
    buttons_frame.grid_rowconfigure(i, weight=1) # weight allows space between each element

# run program
root.mainloop()