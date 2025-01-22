from model.Room.Room import Room


class RoomMutiny(Room):
    def __init__(self, room_id, name, description, picture, status, unit_price, room_type, game_equipment):
        super().__init__(room_id, name, description, picture, status, unit_price, room_type)
        self.game_equipment = game_equipment
    def __str__(self):
        info = f"Information of Room: \n +Room ID: {self.room_id} \n +Name: {self.name} \n +Description: {self.description} \n +Picture: {self.picture} \n +Status: {self.status} \n +Unit price: {self.unit_price} \n +Room Type: {self.room_type} \n +Game Equipment: {self.game_equipment}"
        return info