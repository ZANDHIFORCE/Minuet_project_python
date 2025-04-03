from datetime import datetime, time
class LessonSlot:
    def __init__(self, id:int, student_id:int, teacher_id:int, day:int, time:time):
        self.id = id
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.day = day #korean_weekday = ['월', '화', '수', '목', '금', '토', '일']
        self.time = time

    #Getter Setter
    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, value):
        self.student_id = value

    def get_teacher_id(self):
        return self.teacher_id

    def set_teacher_id(self, value):
        self.teacher_id = value

    def get_day(self):
        return self.day

    def set_day(self, value):
        self.day = value

    def get_time(self):
        return self.time

    def set_time(self, value):
        self.time = value

        
    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "teacher_id": self.teacher_id,
            "day": self.day,
            "time": self.time.strftime("%H:%M"),
        }
    
    @classmethod
    def from_dict(cls, item:dict) -> dict:
        return cls(
        id = item["id"],
        student_id = item["student_id"],
        teacher_id = item["teacher_id"],
        day = item["day"],
        time = datetime.strptime(item["time"], "%H:%M").time()
        )
