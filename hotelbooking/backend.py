import mysql.connector

class HotelManagementSystem:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mETLIFE@2",
            database="sukrit"
        )
        self.cursor = self.db.cursor()

    def book_room(self, guest_id, room_id, check_in, check_out):
        try:
            # Check if the room is available for the given dates
            query = "SELECT * FROM Bookings WHERE RoomID = %s AND ((CheckIn <= %s AND CheckOut >= %s) OR (CheckIn <= %s AND CheckOut >= %s))"
            params = (room_id, check_in, check_in, check_out, check_out)
            self.cursor.execute(query, params)
            bookings = self.cursor.fetchall()
            if bookings:
                print("Room is already booked for the given dates.")
                return False

            # Book the room
            insert_query = "INSERT INTO Bookings (GuestID, RoomID, CheckIn, CheckOut) VALUES (%s, %s, %s, %s)"
            insert_params = (guest_id, room_id, check_in, check_out)
            self.cursor.execute(insert_query, insert_params)
            self.db.commit()
            print("Room booked successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def modify_booking(self, booking_id, new_check_in, new_check_out):
        try:
            # Check if the new dates are valid and don't conflict with existing bookings
            query = "SELECT * FROM Bookings WHERE RoomID = (SELECT RoomID FROM Bookings WHERE BookingID = %s) AND ((CheckIn <= %s AND CheckOut >= %s) OR (CheckIn <= %s AND CheckOut >= %s))"
            params = (booking_id, new_check_in, new_check_in, new_check_out, new_check_out)
            self.cursor.execute(query, params)
            bookings = self.cursor.fetchall()
            if bookings:
                print("Room is already booked for the new dates.")
                return False

            # Modify the booking
            update_query = "UPDATE Bookings SET CheckIn = %s, CheckOut = %s WHERE BookingID = %s"
            update_params = (new_check_in, new_check_out, booking_id)
            self.cursor.execute(update_query, update_params)
            self.db.commit()
            print("Booking modified successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False
    def list_available_rooms(self, check_in, check_out):
    
        try:
            query = "SELECT * FROM Rooms WHERE RoomID NOT IN (SELECT RoomID FROM Bookings WHERE CheckIn <= %s AND CheckOut >= %s)"
            params = (check_out, check_in)
            self.cursor.execute(query, params)
            available_rooms = self.cursor.fetchall()
            return available_rooms
        except Exception as e:
            print("Error:", e)
            return []

    def add_guest(self, first_name, last_name, email, phone):
        try:
            query = "INSERT INTO Guests (FirstName, LastName, Email, Phone) VALUES (%s, %s, %s, %s)"
            params = (first_name, last_name, email, phone)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Guest added successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def update_guest(self, guest_id, first_name, last_name, email, phone):
        try:
            query = "UPDATE Guests SET FirstName = %s, LastName = %s, Email = %s, Phone = %s WHERE GuestID = %s"
            params = (first_name, last_name, email, phone, guest_id)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Guest updated successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def delete_guest(self, guest_id):
        try:
            query = "DELETE FROM Guests WHERE GuestID = %s"
            params = (guest_id,)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Guest deleted successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False

    # Add more backend logic as needed
