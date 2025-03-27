class LessonSlot:
    def __init__(self, day, time, teacher_id):
        self.day = day
        self.time = time
        self.teacher_id = teacher_id
        
    def to_dict(self):
        return {
            "day": self.day,
            "time": self.time,
            "teacher_id": self.teacher_id
        }