from datetime import datetime

class LessonInfo:
    def __init__(self, lesson_id, teacher_id, student_id, datetime):
        self.id = lesson_id
        self.teacher_id = teacher_id
        self.student_id = student_id
        self.datetime = datetime # format: '%Y-%m-%dT%H:%M'
        self.completed = False
        
    def get_id(self)-> int: 
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "student_id": self.student_id,
            "datetime": self.datetime.strftime('%Y-%m-%dT%H:%M')
        }
    
    @classmethod
    def from_dict(cls, item):
        return cls(
            lesson_id = item["id"],
            teacher_id = item["teacher_id"],
            student_id = item["student_id"],
            datetime = datetime.strptime(item["datetime"], '%Y-%m-%dT%H:%M'),
        )

        
   


# {
# "id": 1,
# "student_id": 1,
# "lesson_date": "2025-03-03",
# "teacher_id": 1,
# "time": "15:00"
# }