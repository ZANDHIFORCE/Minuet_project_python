class Teacher:
    def __init__(self, name, subject, teacher_id=None):
        self.id = teacher_id
        self.name = name
        self.subject = subject

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_subject(self):
        return self.subject

    def set_subject(self, value):
        self.subject = value

        
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subject": self.subject
        }
        
    def to_map(self):
        return self.to_dict()
    
    @classmethod
    def from_dict(cls, item):
        return cls(
            id = item["teacher_id"],
            name = ["name"],
            subject = ["subject"],
        )
    
        
#   {
#     "id": 1,
#     "name": "미서T",
#     "subject": "피아노"
#   }