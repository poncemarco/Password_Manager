from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import paste, copy
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = ''.join(password_list) # This is better
    # than this:

    #password = ""
    #for char in password_list:
        #password += char

    password_entry.insert(END, string=password)
    copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_count():
    site = website_entry.get()
    user = user_entry.get()
    password = password_text.get()
    data = [site, user, password]
    if site and user and password != '':
        messagebox.askokcancel(title='site', message=f'These are the details entered: \n user: '
                                                    f'{user}\n '
                                                     f'password: {password}')

        with open('passwords_saved.txt', 'a') as file:
            file.write(f'{site}     |   {user}     |        {password} \n')
    else:
        if site == '':
            missing = 'Site'
        if user == '':
            missing = 'user'
        if password == '':
            missing = 'password'


        messagebox.showwarning(title='You miss something', message=f'You miss the {missing}')


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# Image
canvas = Canvas(width=200, height=200, highlightthickness=False)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Text
website_text = Label(text='Website: ')
website_text.grid(column=0, row=1)

email_text = Label(text='Email/Username: ')
email_text.grid(column=0, row=2)

password_text = Label(text='Password: ')
password_text.grid(column=0, row=3)



# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', command=save_count)
add_button.grid(column=2, row=4)


# Entries
website_entry = Entry(width=35)
website_entry.insert(END, string='Ejemplo: facebook')
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=30)
user_entry.insert(END, string='@gmail.com')
user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=15)
password_entry.grid(column=0, row=3, columnspan=2)




window.mainloop()
