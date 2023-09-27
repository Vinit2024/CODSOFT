import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Set window dimensions (width x height)
        window_width = 300
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")

        # Create and set up widgets
        self.label = tk.Label(root, text="Simple Calculator", font=("Helvetica", 16, "bold"))
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.grid(row=1, column=0, padx=10, pady=5)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.grid(row=2, column=0, padx=10, pady=5)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

        self.operation_label = tk.Label(root, text="Select operation:")
        self.operation_label.grid(row=3, column=0, padx=10, pady=5)
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=4, pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightgray", padx=10, pady=10)
        self.result_label.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    self.result_label.config(text="Error: Division by zero", bg="pink")
                    return
                else:
                    result = num1 / num2
            else:
                self.result_label.config(text="Invalid operation", bg="pink")
                return
            
            self.result_label.config(text=f"Result: {result}", bg="lightgreen")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numbers.", bg="pink")
        
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
