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

    def update_room(self, room_id, room_number, room_type, price_per_night):
        try:
            query = "UPDATE Rooms SET RoomNumber = %s, RoomType = %s, PricePerNight = %s WHERE RoomID = %s"
            params = (room_number, room_type, price_per_night, room_id)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Room updated successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def delete_room(self, room_id):
        try:
            query = "DELETE FROM Rooms WHERE RoomID = %s"
            params = (room_id,)
            self.cursor.execute(query, params)
            self.db.commit()
            print("Room deleted successfully.")
            return True
        except Exception as e:
            print("Error:", e)
            return False
