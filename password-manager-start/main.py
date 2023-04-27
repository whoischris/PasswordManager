from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_entry = website_entry.get()
    log_entry = login_entry.get()
    password = password_entry.get()
    new_data = {
        web_entry: {
            "email": log_entry,
            "password": password,

        }
    }

    if len(web_entry) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Dont leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                load_data = json.load(data)
        except:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data with new data
            load_data.update(new_data)

            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(load_data, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="No details for the website exists")
    else:
        if website in data_file:
            email = data_file[website]["email"]
            password = data_file[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{website} does not have any info")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:", fg="white")
website_label.grid(column=0, row=1)
login_label = Label(text="Email/Username:", fg="white")
login_label.grid(column=0, row=2)
password_label = Label(text="Password:", fg="white")
password_label.grid(column=0, row=3)


website_entry = Entry(width=21, highlightthickness=0, bg="white", fg="black")
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
login_entry = Entry(width=35, highlightthickness=0, bg="white", fg="black")
login_entry.grid(column=1, row=2, columnspan=2)
login_entry.insert(0, "chris@yahoo.com")
password_entry = Entry(width=21, highlightthickness=0, bg="white", fg="black", show="*")
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", bg="white", highlightthickness=0, width=10, command=generate)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, bg="white", highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", bg="white", highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()