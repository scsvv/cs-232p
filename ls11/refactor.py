import random, string, sys
import pyperclip
from tkinter import Tk, IntVar, StringVar, Button, Label, Entry, Spinbox

root = Tk()
password = StringVar()
password_length = IntVar()
all_combinations = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  

def rand_pass_gen():
    str_build = "" 
    for y in range(password_length.get()):
        char_type = random.choice(all_combinations)   
        str_build = str_build + random.choice(char_type)
    password.set(password)

def copy_to_clipboard():
    pyperclip.copy(password.get())

messages = {
    "label1": "Type Password Length", 
    "label2": "Random Ganerated Password", 
    "button1": "Generate Password", 
    "button2": "Copy to Clipboard",
    "title": "Password Generator"
}

settings = {
    "title": 'arial 14 bold', 
    "primary": 'arial 12',
}

view = {

    "footer_label": Label(root, text=messages.get("label2"), font=settings.get("primary"))
}

if __name__ == "__main__":

    root.geometry("400x400")
    root.title(messages.get("title"))

    header_label = Label(root, text=messages.get("label1"), font=settings.get("title")).pack()
    header_input = Spinbox(root, from_=4, to=32, textvariable=password_length, width=24, font=settings.get("primary")).pack()
    Button(root, text=messages.get("button1"), command=rand_pass_gen, font=settings.get("primary"), bg='gray', fg='black', activebackground='lightblue', padx=5, pady=5).pack(pady=20)
    footer = Label(root, text=messages.get("label2"), font=settings.get("primary")).pack(pady=10)
    Entry(root, textvariable=password, width=24, font=settings.get("primary")).pack()
    Button(root, text=messages.get("button2"), width=24, font=settings.get("primary")).pack()
    root.mainloop()