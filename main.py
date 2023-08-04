import random
from tkinter import *
import string
import secrets
from tkinter import messagebox
import pyperclip
import json

password = ''
length = 12


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    symbols = ["!", "$", "%", "?", "*", ".", '&']
    alphabet = string.ascii_letters + string.digits + ''.join(random.choices(symbols, k=2))
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and sum(c in symbols for c in password) >= 2):
            break

    password_box.insert(0, f'{password}')
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_box.get()
    password = password_box.get()
    email = email_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!', message='Please fill out all the fields')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_box.delete(0, END)
            password_box.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_box.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Oops!', message='Email not found in database.\nPlease try again!')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f'{website}', message=f'Log in Info:\n\nEmail: {email}\n\nPassword: {password}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website: ', font=('Arial', 10, 'normal'))
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username: ', font=('Arial', 10, 'normal'))
email_label.grid(column=0, row=2)
password_label = Label(text='Password: ', font=('Arial', 10, 'normal'))
password_label.grid(column=0, row=3)

# inputs
website_box = Entry(width=33, justify='left')
website_box.grid(column=1, row=1)
email_box = Entry(width=54)
email_box.grid(column=1, columnspan=2, row=2)
email_box.insert(0, 'your_email@email.com')
password_box = Entry(width=33, justify='left')
password_box.grid(column=1, row=3)

# buttons
search_button = Button(text="Search", width=16, font=('Arial', 9, 'normal'), command=search_website)
search_button.grid(column=2, row=1)
search_button.config(padx=2, pady=2)
password_button = Button(text='Generate Password', width=16, font=('Arial', 9, 'normal'), command=generate_password)
password_button.grid(column=2, row=3)
password_button.config(padx=2, pady=2)
add_button = Button(text='Add', width=40, font=('Arial', 10, 'normal'), command=add_password)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
