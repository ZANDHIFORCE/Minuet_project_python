class Student:
    def __init__(self, name, progress_sessions=0, total_sessions=0 ,student_id=None):
        self.id = student_id
        self.name = name
        self.progress_sessions = progress_sessions
        self.total_sessions = total_sessions
        
# {
# "id": 1,
# "name": "장예진",
# "total_sessions": 8,
# "progress_sessions": 5
# }