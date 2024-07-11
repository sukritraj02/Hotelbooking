import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from add_room import RoomManagement

class AddRoomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Room")
        self.root.geometry("300x200")

        self.room_manager = RoomManagement()

        self.label_room_number = ttk.Label(root, text="Room Number:")
        self.label_room_number.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_number = ttk.Entry(root)
        self.entry_room_number.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_room_type = ttk.Label(root, text="Room Type:")
        self.label_room_type.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_type = ttk.Entry(root)
        self.entry_room_type.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.label_price_per_night = ttk.Label(root, text="Price Per Night:")
        self.label_price_per_night.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_price_per_night = ttk.Entry(root)
        self.entry_price_per_night.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.btn_add_room = ttk.Button(root, text="Add Room", command=self.add_room)
        self.btn_add_room.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_room(self):
        room_number = self.entry_room_number.get()
        room_type = self.entry_room_type.get()
        price_per_night = self.entry_price_per_night.get()

        if room_number and room_type and price_per_night:
            success = self.room_manager.add_room(room_number, room_type, price_per_night)
            if success:
                messagebox.showinfo("Success", "Room added successfully.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Failed to add room. Please try again.")
        else:
            messagebox.showerror("Error", "All fields are required.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddRoomGUI(root)
    root.mainloop()
