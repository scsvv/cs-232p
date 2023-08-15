from tkinter import *
import pyperclip
import random, string

root = Tk()
root.geometry("400x400")
root.title("Password generator")

pass_len = IntVar()
output_pass = StringVar()
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  

def rand_pass_gen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
    output_pass.set(password)

def copy_to_clipboard():
    pyperclip.copy(output_pass.get())

header = Label(root, text='Type Password Length', font='arial 12 bold').pack(pady=10)
length_input = Spinbox(root, from_=4, to=32, textvariable=pass_len, width=24, font='arial 16').pack()

Button(root, text="Generate Password", command=rand_pass_gen, font='arial 12', bg='gray', fg='black', activebackground='lightblue', padx=5, pady=5).pack(pady=20)

footer = Label(root, text='Random Ganerated Password', font='arial 12 bold').pack(pady=10)
Entry(root, textvariable=output_pass, width=24, font='arial 16').pack()
Button(root, text='Copy to Clipboard', width=24, font='arial 16').pack()

root.mainloop()