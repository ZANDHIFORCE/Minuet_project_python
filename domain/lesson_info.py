from datetime import datetime

class LessonInfo:
    def __init__(self, lesson_id, teacher_id, student_id, datetime, completed):
        self.id = lesson_id
        self.teacher_id = teacher_id
        self.student_id = student_id
        self.datetime = datetime # format: '%Y-%m-%dT%H:%M'
        self.completed = completed
        
    # Getters
    def get_id(self):
        return self.id

    def get_teacher_id(self):
        return self.teacher_id

    def get_student_id(self):
        return self.student_id

    def get_datetime(self):
        return self.datetime

    def is_completed(self):
        return self.completed

    # Setters
    def set_id(self, lesson_id):
        self.id = lesson_id

    def set_teacher_id(self, teacher_id):
        self.teacher_id = teacher_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_datetime(self, datetime):
        self.datetime = datetime

    def set_completed(self, completed: bool):
        self.completed = completed
        
    
    def to_dict(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "student_id": self.student_id,
            "date_time": self.datetime.strftime('%Y-%m-%dT%H:%M'),
            "completed": self.completed
        }
        
    def to_map(self):
        return{
            "id": self.id,
            "teacherId": self.teacher_id,
            "studentId": self.student_id,
            "dateTime": self.datetime.strftime('%Y-%m-%dT%H:%M'),
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, item):
        return cls(
            lesson_id = item["id"],
            teacher_id = item["teacher_id"],
            student_id = item["student_id"],
            datetime = datetime.strptime(item["date_time"], '%Y-%m-%dT%H:%M'),
            completed = item["completed"]
        )

        
   


# {
# "id": 1,
# "student_id": 1,
# "lesson_date": "2025-03-03",
# "teacher_id": 1,
# "time": "15:00"
# }