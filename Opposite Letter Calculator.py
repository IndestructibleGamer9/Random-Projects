import tkinter as tk
import pyperclip as pc

class OppositeWordCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Opposite Word Calculator")
        self.output_text = ''
        self.version = 2.5

        # GUI Components
        self.label = tk.Label(root, text="Enter text to convert", font=("Helvetica", 10))
        self.entry = tk.Text(root, height=4, width=50, font=("Helvetica", 10))
        self.submit_button = tk.Button(root, text='Convert', command=self.get_text, font=("Helvetica", 10))
        self.output = tk.Label(root, text='', font=("Helvetica", 10))
        self.copy_button = tk.Button(root, text='Copy to clipboard', font=("Helvetica", 10), command=self.save_to_clip)
        self.about_button = tk.Button(root, text='About', command=self.about_window, font=("Helvetica", 10))
        self.clear_button = tk.Button(root, text='Clear', command=self.clear_text, font=("Helvetica", 10))
        
        # Grid Placement
        self.label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.submit_button.grid(row=2, column=0, padx=10, pady=5)
        self.output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.copy_button.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
        self.clear_button.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
        self.about_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

    def get_text(self):
        message = self.entry.get("1.0", tk.END).strip()
        self.output_text = self.opp(message)
        self.output.config(text=self.output_text)

    def save_to_clip(self):
        if self.output_text:
            pc.copy(self.output_text)
        else:
            self.output.config(text="No text to save to clipboard!")

    def clear_text(self):
        self.output.config(text="")
        self.entry.delete("1.0", tk.END)        

    def calculate_opposite(self, letter):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        opposite_letter = ''
        if letter in letters:
            index = letters.index(letter)
            opposite_letter = letters[25-index]
        else:
            opposite_letter = letter  # Handles non-alphabetic characters
        return opposite_letter

    def opp(self, word):
        return ''.join(self.calculate_opposite(letter.lower()) if letter.islower() else self.calculate_opposite(letter).upper() for letter in word)

    def clear_text(self):
        self.entry.delete("1.0", tk.END)
        self.output.config(text="")

    def about_window(self):
        about = tk.Toplevel(self.root)
        about.title("About")
        about.geometry("400x300")
        info_text = f"""The Opposite Language Calculator converts sentences 
into their opposite form by reversing the alphabet.
For example, 'a' becomes 'z', 'b' becomes 'y', etc.
This can be used for creating secret messages or simply for fun.
Developed by Will Dunno.
For bugs or feedback, email: 
Version {self.version}"""
        info_label = tk.Label(about, text=info_text, font=("Helvetica", 10), justify=tk.LEFT)
        info_label.pack(padx=10, pady=10)

    def run(self):
        self.root.mainloop()

class MyClass():
    def __init__(self, root):
        self.root = root

    def run(self):
        label = tk.label(root, )    

if __name__ == '__main__':
    root = tk.Tk()
    app = OppositeWordCalculator(root)
    clas = MyClass(root)
    app.run()