from model.Room.Room import Room


class RoomCatharsis(Room):
    def __init__(self, room_id, name, description, picture, status, unit_price, room_type, natural_sound_effects):
        super().__init__(room_id, name, description, picture, status, unit_price, room_type)
        self.natural_sound_effects = natural_sound_effects
    def __str__(self):
        info = f"Information of Room: \n +Room ID: {self.room_id} \n +Name: {self.name} \n +Description: {self.description} \n +Picture: {self.picture} \n +Status: {self.status} \n +Unit price: {self.unit_price} \n +Room Type: {self.room_type} \n +Natural sound effects: {self.natural_sound_effects}"
        return info