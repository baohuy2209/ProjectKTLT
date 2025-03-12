import os
from IO.JSONFileFactory import JSONFileFactory
from model.Room.RoomCatharsis import RoomCatharsis
from model.Room.RoomGenii import RoomGenii
from model.Room.RoomMutiny import RoomMutiny
from model.Room.RoomOasis import RoomOasis


class RoomDAL:
    def __init__(self):
        self.list_room = []
        self.json_factory = JSONFileFactory()
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def get_all_room(self):
        filepath = self.get_filepath("../data/Room.json")
        self.list_room = self.json_factory.read_file(filepath, 'r')
        list_room = []
        for room in self.list_room:
            temp_room = None
            match room["room_type"]:
                case "Catharsis":
                    temp_room = RoomCatharsis(room_id=room["room_id"], name=room["name"], description=room["description"], picture=room["picture"], status=room["status"],unit_price=room["unit_price"], room_type=room["room_type"], natural_sound_effects=room["natural_sound_effects"])
                case "Oasis":
                    temp_room = RoomOasis(room_id=room["room_id"], name=room["name"],
                                              description=room["description"], picture=room["picture"], status=room["status"],
                                              unit_price=room["unit_price"], room_type=room["room_type"],
                                              journal_customization=room["journal_customization"])
                case "Genii":
                    temp_room = RoomGenii(room_id=room["room_id"], name=room["name"],
                                              description=room["description"], picture=room["picture"], status=room["status"],
                                              unit_price=room["unit_price"], room_type=room["room_type"],
                                              musical_instruments=room["musical_instruments"])
                case "Mutiny":
                    temp_room = RoomMutiny(room_id=room["room_id"], name=room["name"],
                                              description=room["description"], picture=room["picture"], status=room["status"],
                                              unit_price=room["unit_price"], room_type=room["room_type"],
                                              game_equipment=room["game_equipment"])
            list_room.append(temp_room)
        self.list_room = list_room
        return self.list_room
    def store_new_room(self, new_room):
        filepath = self.get_filepath("../data/Room.json")
        self.json_factory.write_file(filepath, "w", new_room.__dict__)
    def get_all_catharsis_room(self):
        filepath = self.get_filepath("../data/Room.json")
        list_room = self.json_factory.read_file(filepath, "r")
        list_catharsis_room = []
        for room in list_room:
            if room["room_type"] == "Catharsis":
                temp_room = RoomCatharsis(room_id=room["room_id"], name=room["name"], description=room["description"],
                                          picture=room["picture"], status=room["status"], unit_price=room["unit_price"],
                                          room_type=room["room_type"],
                                          natural_sound_effects=room["natural_sound_effects"])
                list_catharsis_room.append(temp_room)
        return list_catharsis_room
    def get_all_oasis_room(self):
        filepath = self.get_filepath("../data/Room.json")
        list_room = self.json_factory.read_file(filepath, "r")
        list_oasis_room = []
        for room in list_room:
            if room["room_type"] == "Oasis":
                temp_room = RoomOasis(room_id=room["room_id"], name=room["name"],
                                      description=room["description"], picture=room["picture"], status=room["status"],
                                      unit_price=room["unit_price"], room_type=room["room_type"],
                                      journal_customization=room["journal_customization"])
                list_oasis_room.append(temp_room)
        return list_oasis_room
    def get_all_genii_room(self):
        filepath = self.get_filepath("../data/Room.json")
        list_room = self.json_factory.read_file(filepath, "r")
        list_genii_room = []
        for room in list_room:
            if room["room_type"] == "Genii":
                temp_room = RoomGenii(room_id=room["room_id"], name=room["name"],
                                      description=room["description"], picture=room["picture"], status=room["status"],
                                      unit_price=room["unit_price"], room_type=room["room_type"],
                                      musical_instruments=room["musical_instruments"])
                list_genii_room.append(temp_room)
        return list_genii_room
    def get_all_mutiny_room(self):
        filepath = self.get_filepath("../data/Room.json")
        list_room = self.json_factory.read_file(filepath, "r")
        list_mutiny_room = []
        for room in list_room:
            if room["room_type"] == "Mutiny":
                temp_room = RoomMutiny(room_id=room["room_id"], name=room["name"],
                                       description=room["description"], picture=room["picture"], status=room["status"],
                                       unit_price=room["unit_price"], room_type=room["room_type"],
                                       game_equipment=room["game_equipment"])
                list_mutiny_room.append(temp_room)
        return list_mutiny_room
    def check_empty_room(self, list_room):
        list_empty = []
        for room in list_room:
            if room.status == "available":
                list_empty.append(room)
        return list_empty
    def check_catharsis_empty(self):
        list_catharsis_room = self.get_all_catharsis_room()
        return self.check_empty_room(list_catharsis_room)
    def check_oasis_empty(self):
        list_oasis_room = self.get_all_oasis_room()
        return self.check_empty_room(list_oasis_room)
    def check_genii_empty(self):
        list_genii_room = self.get_all_genii_room()
        return self.check_empty_room(list_genii_room)
    def check_mutiny_empty(self):
        list_mutiny_room = self.get_all_mutiny_room()
        return self.check_empty_room(list_mutiny_room)
    def get_room_by_id(self, id):
        list_room = self.get_all_room()
        temp_room = None
        for room in list_room:
            if room.room_id ==id:
                temp_room = room
                break
        return temp_room
    def get_index_room_by_id(self, id):
        list_room = self.get_all_room()
        temp_index = None
        for i in range(len(list_room)):
            if list_room[i].room_id == id:
                temp_index = i
                break
        return temp_index
    def get_unit_price_by_room_type(self, room_type):
        match room_type:
            case "Catharsis":
                return 33000
            case "Genii":
                return 34000
            case "Oasis":
                return 29000
            case "Mutiny":
                return 32000
    def to_dictionary(self, arrData):
        list_dict = []
        for element in arrData:
            list_dict.append(element.__dict__)
        return list_dict
    def update_status_room(self, room_id, new_status):
        filepath = self.get_filepath("../data/Room.json")
        room_to_update = self.get_room_by_id(room_id)
        room_to_update.status = new_status
        index_to_update = self.get_index_room_by_id(room_id)
        self.list_room[index_to_update] = room_to_update
        list_update = self.to_dictionary(self.list_room)
        self.json_factory.update_file(filepath, list_update)