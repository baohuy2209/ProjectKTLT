class Feedback:
    def __init__(self, feedback_id, content, rating, date, user_id, room_id):
        self.feedback_id = feedback_id
        self.content = content
        self.rating = rating
        self.date = date
        self.userid = user_id
        self.room_id = room_id
    def __str__(self):
        info = f"Information: \n +ID: {self.feedback_id} \n +Content: {self.content} \n +Rating: {self.rating} \n +Date: {self.date} \n +User id: {self.user_id} \n +Room id: {self.room_id}"
        return info
