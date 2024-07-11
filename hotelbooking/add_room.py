import mysql.connector

class RoomManagement:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mETLIFE@2",
            database="sukrit"
        )
        self.cursor = self.db.cursor()

    def add_room(self, room_number, room_type, price_per_night):
        try:
            query = "INSERT INTO Rooms (RoomNumber, RoomType, PricePerNight) VALUES (%s, %s, %s)"
            params = (room_number, room_type, price_per_night)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Room added successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False
