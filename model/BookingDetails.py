class BookingDetails:
    def __init__(self, booking_details_id, booking_id, room_id, quantity, unit_price, total_price):
        self.booking_details_id = booking_details_id
        self.booking_id = booking_id
        self.room_id = room_id
        self.quantity=quantity
        self.unit_price = unit_price
        self.total_price = total_price
    def __str__(self):
        info = f"Information: \n +ID: {self.booking_details_id} \n +Booking id: {self.room_id} \n +Room id: {self.room_id} +\n Quantity: {self.quantity} \n +Unit price: {self.unit_price} +Total price: {self.total_price}"
        return info
