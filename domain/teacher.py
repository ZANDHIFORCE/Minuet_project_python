class Teacher:
    def __init__(self, name, subject, teacher_id=None):
        self.id = teacher_id
        self.name = name
        self.subject = subject
        
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subject": self.subject
        }
    
    
        
#   {
#     "id": 1,
#     "name": "미서T",
#     "subject": "피아노"
#   }