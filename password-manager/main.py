
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


upper_case_letters = [chr(i) for i in range(65, 91)]
lower_case_letters = [chr(i) for i in range(97, 123)]

letters = upper_case_letters + lower_case_letters
numbers = [chr(i) for i in range(48, 58)]
special_symbols = [
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', 
    ';', '"', '\'', '<', ',' ,'>', '.', '?', '/'
    ]
numbers = [chr(i) for i in range(48, 58)]
chars = [letters, numbers, special_symbols]


'''
This function uses pseudo-random number generator which is not good for security because one can predict it.
To make this password generator, one needs to use the python's secrets module.
'''
def generate():
    letters_num = random.randint(4, 10)
    digits_num = random.randint(2, 4)
    special_num = random.randint(2, 4)
    char_nums = [letters_num, digits_num, special_num]

    gen_password = []

    while any(char_nums):
        i = random.randint(0, len(chars) - 1)
        
        if not char_nums[i]:
            continue

        gen_password.append(random.choice(chars[i]))
        char_nums[i] -= 1

    random.shuffle(gen_password)
    return ''.join(gen_password)

def generate_password():
    password_gen = generate()
    password_entry.delete(0, END)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():    
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if not website or not username or not password:
        messagebox.showwarning(title='Oops', message="Please fill out all fields.")
        return
    
    is_ok = messagebox.askokcancel(
        title=website, 
        message=f'These are the details you entered: \nusername:{username}\nPassword:{password}\nIs it ok to save?')
    
    if not is_ok:
        return
    
   
    try: 
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('passwords.json', 'w') as file:
            data = {
                website: {
                "username": username,
                "password": password
                }
            }
            json.dump(data, file, indent= 4)
    else:
        data[website] = {
                "username": username,
                "password": password
            }
        with open('passwords.json', 'w') as file:
            json.dump(data, file, indent=4)
    finally:
        website_entry.delete(0, END)
        username_entry.delete(0,END)
        username_entry.insert(0, 'blaisemahoro1@gmail.com')
        password_entry.delete(0, END)
        website_entry.focus()
        
        
    
def search():
    website = website_entry.get()
    
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            record = data[website]
            username = record['username']
            password = record['password']
            messagebox.showwarning(title=website, message=f'Username: {username}\nPassword: {password}')
    except FileNotFoundError:
        messagebox.showwarning(title='Oops', message="Unable to find password")
        
    except KeyError:
        messagebox.showwarning(title='Oops', message="Unable to find password")
        
             
                

        
   
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry(width=27)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'blaisemahoro1@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text='Search', command=search, width=13)
search_button.grid(row=1, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()