import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.manage_room import RoomManagement

class ManageRoomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Room")
        self.root.geometry("300x200")

        self.room_manager = RoomManagement()

        self.label_room_id = ttk.Label(root, text="Room ID:")
        self.label_room_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_id = ttk.Entry(root)
        self.entry_room_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_room_number = ttk.Label(root, text="Room Number:")
        self.label_room_number.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_number = ttk.Entry(root)
        self.entry_room_number.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.label_room_type = ttk.Label(root, text="Room Type:")
        self.label_room_type.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_type = ttk.Entry(root)
        self.entry_room_type.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.label_price_per_night = ttk.Label(root, text="Price Per Night:")
        self.label_price_per_night.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_price_per_night = ttk.Entry(root)
        self.entry_price_per_night.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.btn_update_room = ttk.Button(root, text="Update Room", command=self.update_room)
        self.btn_update_room.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.btn_delete_room = ttk.Button(root, text="Delete Room", command=self.delete_room)
        self.btn_delete_room.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def update_room(self):
        room_id = self.entry_room_id.get()
        room_number = self.entry_room_number.get()
        room_type = self.entry_room_type.get()
        price_per_night = self.entry_price_per_night.get()

        if room_id and room_number and room_type and price_per_night:
            success = self.room_manager.update_room(room_id, room_number, room_type, price_per_night)
            if success:
                messagebox.showinfo("Success", "Room updated successfully.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Failed to update room. Please try again.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def delete_room(self):
        room_id = self.entry_room_id.get()

        if room_id:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this room?")
            if confirm:
                success = self.room_manager.delete_room(room_id)
                if success:
                    messagebox.showinfo("Success", "Room deleted successfully.")
                    self.root.destroy()
                else:
                    messagebox.showerror("Error", "Failed to delete room. Please try again.")
        else:
            messagebox.showerror("Error", "Room ID is required.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ManageRoomGUI(root)
    root.mainloop()
