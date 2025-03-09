from sympy import print_tree

from data_access_layer.RoomDAL import RoomDAL

room_dal = RoomDAL()
list_room = room_dal.get_all_room()
for room in list_room:
    print(room)

list_catharsis_room = room_dal.get_all_catharsis_room()
for room in list_catharsis_room:
    print(room)

print(room_dal.get_unit_price_by_room_type("Genii"))
room_dal.update_status_room("catharsis5", "full")