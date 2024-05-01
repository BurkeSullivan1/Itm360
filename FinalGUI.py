### Burke Sullivan

### Final GUI

### Tkinter
from FinalDb import create_user
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, Frame, Toplevel, PhotoImage
import requests

class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("750x500")
        self.window.title("Login System")
        self.current_user = None
        #requests session
        self.session = requests.Session()

        # GUI code for the background image using Pillow
        pilImage = Image.open("family.png")  # Load the image file
        self.image = ImageTk.PhotoImage(pilImage)  # Convert the image for Tkinter
        self.bg_image = Label(window, image=self.image)
        self.bg_image.place(relx=0, rely=0, relwidth=1, relheight=1)

        # GUI code for top login banner, changed to green background
        topBanner = Frame(window, bg="dark green")
        topBanner.place(relx=0, rely=0.02, relwidth=1, relheight=0.15)
        welcome = Label(topBanner, text="Life Insurance - Login ", bg="dark green", fg="white", font=("Times New Roman", 25, "bold"))
        welcome.place(relx=0.35, rely=0.28)

        # GUI code for buttons and inputs frame, changed to a lighter green
        buttonFrame = Frame(window, bg="light green")
        buttonFrame.place(relx=0.04, rely=0.2, relwidth=0.5, relheight=0.75)

        # Misc label
        misc = Label(buttonFrame, text="---- OR ----", bg="light green", fg="black", font=("Times New Roman", 14, "bold"))
        misc.place(relx=0.35, rely=0.65)

        # Buttons for sign-in and create account with adjusted colors
        # Login button setup
        self.loginButton = Button(window, text="Login", font=("Times New Roman", 15, "bold"), command=self.login)
        self.loginButton.place(relx=0.2, rely=0.55, relwidth=0.6)
        self.createAccount = Button(buttonFrame, text="Create an Account", bg="dark green", fg="white",
                                    font=("Times New Roman", 15, "bold"), command=self.newAccount)
        self.createAccount.place(relx=0.2, rely=0.85, relwidth=0.6)

        # Labels and entries for username and password with updated background colors
        Label(buttonFrame, text="Username", bg="light green", fg="black", font=("Times New Roman", 16, "bold")).place(relx=0.025, rely=0.1)
        self.usernameEntry = Entry(buttonFrame, bg="white")
        self.usernameEntry.place(relx=0.025, rely=0.18, relwidth=0.4)

        Label(buttonFrame, text="Password", bg="light green", fg="black", font=("Times New Roman", 16, "bold")).place(relx=0.025, rely=0.3)
        self.passwordEntry = Entry(buttonFrame, bg="white", show="*")
        self.passwordEntry.place(relx=0.025, rely=0.38, relwidth=0.4)


# Password visibility toggle with updated icons and background
        self.openeyePic = PhotoImage(file="openeye.png")  # Adjust path as necessary
        self.closedeyePic = PhotoImage(file="closedeye.png")  # Adjust path as necessary
        self.togglepassword = Button(buttonFrame, image=self.closedeyePic, bg="light green", command=self.show_password)
        self.togglepassword.place(relx=0.43, rely=0.38, relwidth=0.06, relheight=0.06)

    def show_password(self):
        if self.passwordEntry.cget('show') == '':
            self.passwordEntry.config(show='*')
            self.togglepassword.config(image=self.closedeyePic)
        else:
            self.passwordEntry.config(show='')
            self.togglepassword.config(image=self.openeyePic)
# login functionality
    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        try:
            response = requests.post('http://127.0.0.1:5000/login', data={'username': username, 'password': password})
            data = response.json()
            if data.get('success'):
                messagebox.showinfo("Login Success", "You are logged in.")
                self.current_user = {
                    'id': data['id'],
                    'username': username,
                    'age': data['age'],
                    'insurance_type': data['insurance_type']
                }
                self.show_insurance(data['insurance_type'], data['age'])
            else:
                messagebox.showerror("Login Failed", data.get('message', 'Login failed with no error message.'))
        except requests.exceptions.ConnectionError as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {str(e)}")
        except ValueError:  # This captures JSON decoding errors
            messagebox.showerror("Error", "Invalid response from server, unable to decode.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    ### show insurance protected window
    def show_insurance(self, insurance_type, age):
        insurance_window = Toplevel(self.window)
        insurance_window.title("Insurance Details")
        insurance_window.geometry("300x150")

        # Insurance type label
        insurance_label = tk.Label(insurance_window, text=f"Your Insurance Type: {insurance_type}", font=("Times New Roman", 14))
        insurance_label.pack(pady=(20, 0))

        # Age and recommended plan label
        plan = "Basic Plan" if int(age) < 20 else "Gold Plan"
        age_plan_label = tk.Label(insurance_window, text=f"Age: {age} - Recommended Plan: {plan}", font=("Times New Roman", 14))
        age_plan_label.pack(pady=(10, 20))

        # Dropdown to modify insurance type
        modify_label = tk.Label(insurance_window, text="Modify your insurance plan:", font=("Times New Roman", 12))
        modify_label.pack()
        insurance_options = ["Whole Life", "Term-Life", "Basic Plan", "Gold Plan"]  # Adding options for plans
        insurance_var = tk.StringVar(insurance_window)
        insurance_var.set(insurance_type)  # default value
        insurance_menu = tk.OptionMenu(insurance_window, insurance_var, *insurance_options)
        insurance_menu.pack()

        # Button to update insurance plan
        update_button = tk.Button(insurance_window, text="Update Plan", font=("Times New Roman", 12), command=lambda: self.update_insurance_plan(insurance_var.get()))
        update_button.pack(pady=10)

    def update_insurance_plan(self, new_plan):
        if not self.current_user:
            messagebox.showerror("Error", "No user session found. Please log in.")
            return

        user_id = self.current_user['id']
        try:
            response = requests.post('http://127.0.0.1:5000/update_plan', data={'user_id': user_id, 'new_plan': new_plan})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Your insurance plan has been updated successfully.")
                self.current_user['insurance_type'] = new_plan  # Update the local session copy
            else:
                messagebox.showerror("Update Failed", f"Failed to update your insurance plan: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {str(e)}")


    def newAccount(self):
        passwindow = tk.Toplevel(self.window)
        passwindow.title("Create New Account")
        passwindow.geometry("300x350")
        passwindow.configure(bg='dark green')

        # Email label and entry box
        email = tk.Label(passwindow, text="Email Address", font=("Tibetan Machine Uni", 11, "bold"), bg='light green')
        email.place(relx=0.05, rely=0.1)
        self.emailbox = tk.Entry(passwindow)
        self.emailbox.place(relwidth=0.6, relx=0.04, rely=0.16)

        # Username label and entry box
        userid = tk.Label(passwindow, text="Username", font=("Tibetan Machine Uni", 11, "bold"), bg='light green')
        userid.place(relx=0.05, rely=0.26)
        self.useridbox = tk.Entry(passwindow)
        self.useridbox.place(relwidth=0.6, relx=0.04, rely=0.32)

        # Password label and entry box
        newPassword = tk.Label(passwindow, text="Create Password", font=("Tibetan Machine Uni", 11, "bold"), bg='light green')
        newPassword.place(relx=0.05, rely=0.42)
        self.newPasswordbox = tk.Entry(passwindow, show="*")
        self.newPasswordbox.place(relwidth=0.6, relx=0.04, rely=0.48)

        # Age input field
        ageLabel = tk.Label(passwindow, text="Age", font=("Tibetan Machine Uni", 11, "bold"), bg='light green')
        ageLabel.place(relx=0.05, rely=0.54)
        self.agebox = tk.Entry(passwindow)
        self.agebox.place(relwidth=0.6, relx=0.04, rely=0.6)

        # Insurance Type Dropdown
        insuranceLabel = tk.Label(passwindow, text="Select Insurance Type", fg="black", font=("Tibetan Machine Uni", 11, "bold"), bg='light green')
        insuranceLabel.place(relx=0.05, rely=0.66)
        insuranceTypes = ["Whole Life", "Term-Life"]
        self.insuranceTypeVar = tk.StringVar(passwindow)
        self.insuranceTypeVar.set(insuranceTypes[0])  # default value
        insuranceMenu = tk.OptionMenu(passwindow, self.insuranceTypeVar, *insuranceTypes)
        insuranceMenu.place(relwidth=0.6, relx=0.04, rely=0.72)

        # Sign Up button
        signup = tk.Button(passwindow, text="Sign Up", font=("Tibetan Machine Uni", 11, "bold"), command=self.signupTkinter)
        signup.place(relwidth=0.6, relx=0.04, rely=0.82)



### Sign up
    def signupTkinter(self):
        user_id = self.useridbox.get()
        email = self.emailbox.get()
        password = self.newPasswordbox.get()
        insurance_type = self.insuranceTypeVar.get()
        user_age = self.agebox.get()  # Retrieve age from the age input field

        if not all([user_id, email, password, insurance_type, user_age]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            create_user(email, password, insurance_type, user_age)  # Pass age to the user creation function
            messagebox.showinfo("Success", "Your account has been created successfully!")
        except Exception as e:
            messagebox.showerror("Signup Failed", str(e))

### RUN program
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
