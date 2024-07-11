import mysql.connector

class GuestManagement:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mETLIFE@2",
            database="sukrit"
        )
        self.cursor = self.db.cursor()

    def get_all_guests(self):
        try:
            query = "SELECT * FROM Guests"
            self.cursor.execute(query)
            guests = self.cursor.fetchall()
            return guests
        except Exception as e:
            print("Error:", e)
            return []

