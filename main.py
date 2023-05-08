import tkinter as tk
import json
import messagebox as message


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    import random
    import string
    password_list = []
    for _ in range(0, 5):
        password_list.append(random.choice(string.ascii_letters))
    for _ in range(0, 3):
        password_list.append(random.choice(string.punctuation))
    for _ in range(0, 2):
        password_list.append(random.choice(string.digits))
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.txt", "r") as data_file:
            data = data_file.readlines()
            for line in data:
                if website in line:
                    print(line)
    except FileNotFoundError:
        print("File not found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }

    if len(website) == 0 or len(password) == 0:
        message.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
canvas.grid(column=1, row=1)

logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=2)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=3)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=4)

# Entries
search_button = tk.Button(text="Search", width=14, command=search)
search_button.grid(column=3, row=2)

website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=4)

# Buttons
search_button = tk.Button(text="Search", width=14, command=search)
search_button.grid(column=3, row=2)

generate_password_button = tk.Button(text="Generate Password", command=generate_random_password)
generate_password_button.grid(column=3, row=4, columnspan=2)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
