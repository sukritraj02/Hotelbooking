import tkinter as tk
from tkinter import ttk
from backend.view_guests import GuestManagement

class ViewGuestsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("View Guests")
        self.root.geometry("400x300")

        self.guest_manager = GuestManagement()

        self.tree = ttk.Treeview(root, columns=("Guest ID", "First Name", "Last Name", "Email", "Phone"), show="headings")
        self.tree.heading("Guest ID", text="Guest ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone", text="Phone")
        self.tree.pack(fill="both", expand=True)

        self.populate_guests()

    def populate_guests(self):
        guests = self.guest_manager.get_all_guests()
        for guest in guests:
            self.tree.insert("", "end", values=guest)

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewGuestsGUI(root)
    root.mainloop()
