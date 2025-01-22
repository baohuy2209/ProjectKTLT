from model.Room.Room import Room


class RoomOasis(Room):
    def __init__(self, room_id, name, description, picture, status, unit_price, room_type, journal_customization):
        super().__init__(room_id, name, description, picture, status, unit_price, room_type)
        self.journal_customization = journal_customization
    def __str__(self):
        info = f"Information of Room: \n +Room ID: {self.room_id} \n +Name: {self.name} \n +Description: {self.description} \n +Picture: {self.picture} \n +Status: {self.status} \n +Unit price: {self.unit_price} \n +Room Type: {self.room_type} \n +Journal Customization: {self.journal_customization}"
        return info