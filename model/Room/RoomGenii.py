from model.Room.Room import Room


class RoomGenii(Room):
    def __init__(self, room_id, name, description, picture, status, unit_price, room_type, music_instruments):
        super().__init__(room_id, name, description, picture, status, unit_price, room_type)
        self.music_instruments = music_instruments
    def __str__(self):
        info = f"Information of Room: \n +Room ID: {self.room_id} \n +Name: {self.name} \n +Description: {self.description} \n +Picture: {self.picture} \n +Status: {self.status} \n +Unit price: {self.unit_price} \n +Room Type: {self.room_type} \n +Music Instruments: {self.music_instruments}"
        return info