import tkinter as tk
from tkinter import ttk
from backend.view_bookings import BookingManagement

class ViewBookingsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("View Bookings")
        self.root.geometry("400x300")

        self.booking_manager = BookingManagement()

        self.tree = ttk.Treeview(root, columns=("Booking ID", "Guest ID", "Room ID", "Check-in", "Check-out"), show="headings")
        self.tree.heading("Booking ID", text="Booking ID")
        self.tree.heading("Guest ID", text="Guest ID")
        self.tree.heading("Room ID", text="Room ID")
        self.tree.heading("Check-in", text="Check-in")
        self.tree.heading("Check-out", text="Check-out")
        self.tree.pack(fill="both", expand=True)

        self.populate_bookings()

    def populate_bookings(self):
        bookings = self.booking_manager.get_all_bookings()
        for booking in bookings:
            self.tree.insert("", "end", values=booking)

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewBookingsGUI(root)
    root.mainloop()
