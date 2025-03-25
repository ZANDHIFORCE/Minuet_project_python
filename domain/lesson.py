from datetime import datetime

class Lesson:
    def __init__(self, lesson_id, teacher_id, student_id, lesson_datetime):
        self.id = lesson_id
        self.teacher_id = teacher_id
        self.student_id = student_id
        self.lesson_datetime = lesson_datetime
    
    def to_dict(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "student_id": self.student_id,
            "lesson_datetime": self.lesson_datetime.strftime('%Y-%m-%dT%H:%M')
        }


# {
# "id": 1,
# "student_id": 1,
# "lesson_date": "2025-03-03",
# "teacher_id": 1,
# "time": "15:00"
# }