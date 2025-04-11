class Student:
    def __init__(self, name, progress_sessions=0, total_sessions=0 ,student_id=None):
        self.id = student_id
        self.name = name
        self.progress_sessions = progress_sessions
        self.total_sessions = total_sessions
        
    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_progress_sessions(self):
        return self.progress_sessions

    def get_total_sessions(self):
        return self.total_sessions

    def get_lesson_slots(self):
        return self.lesson_slots

    # Setters
    def set_id(self, student_id):
        self.id = student_id

    def set_name(self, name):
        self.name = name

    def set_progress_sessions(self, progress_sessions):
        self.progress_sessions = progress_sessions

    def set_total_sessions(self, total_sessions):
        self.total_sessions = total_sessions

    def add_lesson_slot(self, lesson_slot):
        self.lesson_slots.append(lesson_slot)
    
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "total_sessions": self.total_sessions,
            "progress_sessions": self.progress_sessions,
        }
    
    def to_map(self):
        return {
            "id": self.id,
            "name": self.name,
            "totalSessions": self.total_sessions,
            "progressSessions": self.progress_sessions,
        }        
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["id"],
            name=data["name"],
            total_sessions=data["total_sessions"],
            progress_sessions=data["progress_sessions"]
        )
        
# {
# "id": 1,
# "name": "장예진",
# "total_sessions": 8,
# "progress_sessions": 5
# }