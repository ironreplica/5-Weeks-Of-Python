from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# Random Password
def generatePassword():
    # Constant variables for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    password_list = []

    # Without List comprehension
    # for char in range(num_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(num_symbols):
    #     password_list += (random.choice(symbols))
    #
    # for char in range(num_numbers):
    #     password_list += (random.choice(numbers))

    # With List Comprehension
    password_list += [random.choice(letters) for char in range(num_letters)]
    password_list += [random.choice(symbols) for char in range(num_symbols)]
    password_list += [random.choice(numbers) for char in range(num_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Save password
def onSave():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) > 0 or len(email) > 0 or len(password) > 0:
        # If this file does not exist, it will be creaated.
        accept = messagebox.askokcancel(title="Save password?",
                                        message=f'{website} Login Credentials \nEmail: {email} \nPassword: {password} \nSave?')
        if accept:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please fill out all fields.")

# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1)
email_label = Label(text='Email/Username:')
email_label.grid(row=2)
password_label = Label(text='Password:')
password_label.grid(row=3)

# Entries
website_entry = Entry(width= 35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'trevorchilds8@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text='Generate Password', command=generatePassword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=onSave)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
