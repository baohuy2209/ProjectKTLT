from data_access_layer.BookingOrderDAL import BookingOrderDAL

booking_order_dal = BookingOrderDAL()
list_bo = booking_order_dal.get_all_booking_order()
for bo in list_bo:
    print(bo)
booking_order_dal.book_room()