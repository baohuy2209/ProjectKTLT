class Room:
    def __init__(self, room_id, name, description, picture, status, unit_price, room_type):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.picture = picture
        self.status = status
        self.unit_price = unit_price
        self.room_type = room_type
    def __str__(self):
        info = f"Information of Room: \n +Room ID: {self.room_id} \n +Name: {self.name} \n +Description: {self.description} \n +Picture: {self.picture} \n +Status: {self.status} \n +Unit price: {self.unit_price} \n +Room Type: {self.room_type}"
        return info
