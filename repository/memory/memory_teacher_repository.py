import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from repository.interface.teacher_repository_interface import TeacherRepositoryInterface
from domain.teacher import Teacher
from typing import List
import json

class MemoryTeacherRepository(TeacherRepositoryInterface):
    def __init__(self):
        self.teachers = {}
    
    def load_from_file(self, path=f"{BASE_DIR}/data/teachers.json"):
        with open(path,'r',encoding='utf-8') as file:
            data = json.load(file)
            for teacher in data:
                id = teacher["id"]
                name = teacher["name"]
                subject = teacher["subject"]
                self.create_teacher(Teacher(name,subject,id))
    
    def save_to_file(self, path=f"{BASE_DIR}/data/teachers.json"):
        with open(path,'w',encoding='utf-8') as file:
           teachers = [ teacher.to_dict() for teacher in self.teachers.values()]
           json.dump(teachers, file, ensure_ascii=False, indent = 4)
    
    def clearStore(self) -> None:
        self.teachers.clear()
        
    #Implement the methods from the interface
    def get_length(self) -> int:
        return len(self.teachers)
    
    def get_teacher(self, teacher_id: int) -> Teacher:
        if teacher_id not in self.teachers:
            raise KeyError(f"Teacher with id {teacher_id} doesn't exist.")
        return self.teachers[teacher_id]

    def get_teachers(self) -> List[Teacher]:
        return list(self.teachers.values())

    def create_teacher(self, teacher: Teacher) -> Teacher:
        if teacher.id in self.teachers:
            raise ValueError(f"Teacher with id {teacher.get_id()} already exist.")
        self.teachers[teacher.id] = teacher
        return teacher

    def update_teacher(self, teacher: Teacher) -> Teacher:
        if teacher.id not in self.teachers:
            raise ValueError(f"Teacher with id {teacher.get_id()} doesn't exist.")
        self.teachers[teacher.id] = teacher
        return teacher

    def delete_teacher(self, teacher_id: int) -> None:
        if teacher_id not in self.teachers:
            raise KeyError(f"Cannot delete: no teacher with id {teacher_id}")
        del self.teachers[teacher_id]

