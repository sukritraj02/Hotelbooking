import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend import HotelManagementSystem;
# Assuming HotelManagementSystem class is in a separate file

class HotelManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("400x300")

        self.hotel_system = HotelManagementSystem()  # Initialize the backend system

        # Guest ID Entry
        self.label_guest_id = ttk.Label(root, text="Guest ID:")
        self.label_guest_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_guest_id = ttk.Entry(root)
        self.entry_guest_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Room ID Entry
        self.label_room_id = ttk.Label(root, text="Room ID:")
        self.label_room_id.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_room_id = ttk.Entry(root)
        self.entry_room_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Check-in Entry
        self.label_check_in = ttk.Label(root, text="Check-in Date (YYYY-MM-DD):")
        self.label_check_in.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_check_in = ttk.Entry(root)
        self.entry_check_in.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Check-out Entry
        self.label_check_out = ttk.Label(root, text="Check-out Date (YYYY-MM-DD):")
        self.label_check_out.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_check_out = ttk.Entry(root)
        self.entry_check_out.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Book Room Button
        self.btn_book_room = ttk.Button(root, text="Book Room", command=self.book_room)
        self.btn_book_room.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # Booking ID Entry for Modification
        self.label_booking_id = ttk.Label(root, text="Booking ID:")
        self.label_booking_id.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_booking_id = ttk.Entry(root)
        self.entry_booking_id.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # New Check-in Entry for Modification
        self.label_new_check_in = ttk.Label(root, text="New Check-in Date (YYYY-MM-DD):")
        self.label_new_check_in.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_new_check_in = ttk.Entry(root)
        self.entry_new_check_in.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # New Check-out Entry for Modification
        self.label_new_check_out = ttk.Label(root, text="New Check-out Date (YYYY-MM-DD):")
        self.label_new_check_out.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.entry_new_check_out = ttk.Entry(root)
        self.entry_new_check_out.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        # Modify Booking Button
        self.btn_modify_booking = ttk.Button(root, text="Modify Booking", command=self.modify_booking)
        self.btn_modify_booking.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def book_room(self):
        guest_id = self.entry_guest_id.get()
        room_id = self.entry_room_id.get()
        check_in = self.entry_check_in.get()
        check_out = self.entry_check_out.get()

        if guest_id and room_id and check_in and check_out:
            success = self.hotel_system.book_room(int(guest_id), int(room_id), check_in, check_out)
            if success:
                messagebox.showinfo("Success", "Room booked successfully.")
            else:
                messagebox.showerror("Error", "Failed to book room. Please try again.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def modify_booking(self):
        booking_id = self.entry_booking_id.get()
        new_check_in = self.entry_new_check_in.get()
        new_check_out = self.entry_new_check_out.get()

        if booking_id and new_check_in and new_check_out:
            success = self.hotel_system.modify_booking(int(booking_id), new_check_in, new_check_out)
            if success:
                messagebox.showinfo("Success", "Booking modified successfully.")
            else:
                messagebox.showerror("Error", "Failed to modify booking. Please try again.")
        else:
            messagebox.showerror("Error", "All fields are required.")



    def list_available_rooms(self):
        check_in = self.entry_check_in.get()
        check_out = self.entry_check_out.get()

        if check_in and check_out:
            available_rooms = self.hotel_system.list_available_rooms(check_in, check_out)
            if available_rooms:
                room_numbers = [str(room[0]) for room in available_rooms]
                messagebox.showinfo("Available Rooms", "Available Rooms: " + ", ".join(room_numbers))
            else:
                messagebox.showinfo("Available Rooms", "No available rooms for the selected dates.")
        else:
            messagebox.showerror("Error", "Please enter check-in and check-out dates.")

    def add_guest(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if first_name and last_name:
            success = self.hotel_system.add_guest(first_name, last_name, email, phone)
            if success:
                messagebox.showinfo("Success", "Guest added successfully.")
                self.clear_guest_entries()
            else:
                messagebox.showerror("Error", "Failed to add guest. Please try again.")
        else:
            messagebox.showerror("Error", "First name and last name are required.")

    def update_guest(self):
        guest_id = self.entry_guest_id.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if guest_id and first_name and last_name:
            success = self.hotel_system.update_guest(int(guest_id), first_name, last_name, email, phone)
            if success:
                messagebox.showinfo("Success", "Guest updated successfully.")
            else:
                messagebox.showerror("Error", "Failed to update guest. Please try again.")
        else:
            messagebox.showerror("Error", "Guest ID, first name, and last name are required.")

    def delete_guest(self):
        guest_id = self.entry_guest_id.get()

        if guest_id:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this guest?")
            if confirm:
                success = self.hotel_system.delete_guest(int(guest_id))
                if success:
                    messagebox.showinfo("Success", "Guest deleted successfully.")
                    self.clear_guest_entries()
                else:
                    messagebox.showerror("Error", "Failed to delete guest. Please try again.")
        else:
            messagebox.showerror("Error", "Guest ID is required.")
 

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementGUI(root)
    root.mainloop()
