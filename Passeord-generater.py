import tkinter as tk
import string
import random

def generate_password(length, complexity):
    characters = ""
    
    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Set window dimensions (width x height)
        window_width = 400
        window_height = 250
        self.root.geometry(f"{window_width}x{window_height}")

        # Create and set up widgets
        self.label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
        self.label.pack(fill=tk.X)

        self.length_label = tk.Label(root, text="Enter Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Select Complexity:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Low")

        self.low_complexity_radio = tk.Radiobutton(root, text="Low", variable=self.complexity_var, value="Low")
        self.medium_complexity_radio = tk.Radiobutton(root, text="Medium", variable=self.complexity_var, value="Medium")
        self.high_complexity_radio = tk.Radiobutton(root, text="High", variable=self.complexity_var, value="High")

        self.low_complexity_radio.pack()
        self.medium_complexity_radio.pack()
        self.high_complexity_radio.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
        self.result_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.result_label = tk.Label(self.result_frame, text="", bg="white", wraplength=window_width-20)
        self.result_label.pack(fill=tk.BOTH, expand=True)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.result_label.config(text="Password length must be greater than zero.")
            else:
                complexity = self.complexity_var.get()
                password = generate_password(length, complexity)
                self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number for password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
