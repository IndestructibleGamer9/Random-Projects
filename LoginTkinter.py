import sqlite3
import os
import tkinter as tk

DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='white', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self._focus_in)
        self.bind("<FocusOut>", self._focus_out)

        self._put_placeholder()

    def _put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def _focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def _focus_out(self, event):
        if not self.get():
            self._put_placeholder()

class App():
    def __init__(self):
        #Database Conncetion
        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()
        self.root = tk.Tk()

    def submit(self):
        #get data
        # get database 
        # check if data = database
        username_entry = self.usernameEntery.get()
        password_entry = self.passwordEntery.get()
        self.usernameEntery.delete(0, 'end')
        self.passwordEntery.delete(0, 'end')
        
        self.c.execute("SELECT username FROM Users")
        dbUsername = self.c.fetchone()
        self.c.execute("SELECT password FROM Users")
        dbPassword = self.c.fetchone()

        duc = dbUsername[0].strip("(),'")
        dpc = dbPassword[0].strip("(),'")

        if str(duc) == str(username_entry):
            
            print("Usernames Match")
            if dpc == password_entry:
                print("Password Match")
                print("Entery Granted")
                self.main()
                self.login.destroy()
            else:
                print("usernames match passwords do not")    
        else:
            print("username does not match") 
            print(f"username database: {duc} is not = {username_entry}")       

    def clean_up(self):
        pass



    def setup(self):
        self.root.withdraw()
        self.login = tk.Toplevel(self.root, bg='#5B859E')
        self.login.title("Login")
        self.login.geometry('250x150')
        self.titleText = tk.Label(self.login, text='Login', font=('Yu Gothic UI Semibold', 14), bg='#5B859E', fg='white')
        self.usernameEntery = PlaceholderEntry(self.login, 'Username', bg='#5B859E')
        self.passwordEntery = PlaceholderEntry(self.login, 'Password', bg='#5B859E', show="*")
        self.submitButton = tk.Button(self.login, 
                                      text='Submit', 
                                      font=('Yu Gothic UI Semibold', 10), 
                                      bg='#5B859E', fg='white', 
                                      borderwidth=0, highlightthickness=10, overrelief='flat',
                                      command=self.submit)

        self.titleText.pack(padx=5, pady=5)  
        self.usernameEntery.pack(padx=5, pady=5)   
        self.passwordEntery.pack(padx=5, pady=5) 
        self.submitButton.pack(padx=5, pady=5) 


    def main(self):
        self.root.deiconify()



    def run(self):
        self.setup()
        self.root.mainloop()    

if __name__ == "__main__":
    entry = App()
    entry.run()
    
