from data_access_layer.BookingDetailsDAL import BookingDetailsDAL

bd_dal = BookingDetailsDAL()
list_bd = bd_dal.get_all_booking_detail()
for bd in list_bd:
    print(bd)