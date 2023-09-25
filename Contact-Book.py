import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Set window dimensions (width x height)
        window_width = 400
        window_height = 300
        root.geometry(f"{window_width}x{window_height}")

        # Create and set up widgets
        self.label = tk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold"), bg="green", fg="white")
        self.label.pack(fill=tk.X)

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        self.add_button.bind("<Enter>", self.button_hover_enter)
        self.add_button.bind("<Leave>", self.button_hover_leave)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()
        self.view_button.bind("<Enter>", self.button_hover_enter)
        self.view_button.bind("<Leave>", self.button_hover_leave)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()
        self.delete_button.bind("<Enter>", self.button_hover_enter)
        self.delete_button.bind("<Leave>", self.button_hover_leave)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        self.quit_button.bind("<Enter>", self.button_hover_enter)
        self.quit_button.bind("<Leave>", self.button_hover_leave)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Name and phone fields cannot be empty.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact book is empty.")
        else:
            contacts_list = "\n".join(f"Name: {name}, Phone: {phone}" for name, phone in self.contacts)
            messagebox.showinfo("Contacts", contacts_list)

    def delete_contact(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact book is empty.")
        else:
            name_to_delete = self.name_entry.get()
            for i, (name, phone) in enumerate(self.contacts):
                if name == name_to_delete:
                    del self.contacts[i]
                    self.update_contact_listbox()
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    self.name_entry.delete(0, tk.END)
                    return
            messagebox.showerror("Error", "Contact not found.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in self.contacts:
            self.contact_listbox.insert(tk.END, f"Name: {name}, Phone: {phone}")

    def button_hover_enter(self, event):
        event.widget.config(bg="blue")

    def button_hover_leave(self, event):
        event.widget.config(bg="SystemButtonFace")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
