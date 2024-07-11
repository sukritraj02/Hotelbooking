import mysql.connector

class BookingManagement:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mETLIFE@2",
            database="sukrit"
        )
        self.cursor = self.db.cursor()

    def get_all_bookings(self):
        try:
            query = "SELECT * FROM Bookings"
            self.cursor.execute(query)
            bookings = self.cursor.fetchall()
            return bookings
        except Exception as e:
            print("Error:", e)
            return []
