import random
import string
import secrets
from tkinter import *
from tkinter import ttk


class PasswordGenerator:

    def __init__(self, master : Tk) -> None:
        self.pass_len = 16
        self.char_set = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
        master.title("Password Generator")
        self.len_entry = ttk.Entry(master, width=30)
        self.len_entry.pack()

    
    def produce_random_pass(self) -> str:
        password = []
        for _ in range(self.pass_len):
            password.append(secrets.choice(self.char_set))
        
        random.shuffle(password)

        return str.join("", password)

if __name__ == "__main__":
    root = Tk()
    passGen = PasswordGenerator(root)
    root.mainloop()


