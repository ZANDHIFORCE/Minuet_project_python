import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from repository.interface.student_repository_interface import StudentRepositoryInterface
from domain.student import Student
from typing import List
import json
from domain.student import Student

class MemoryStudentRepository(StudentRepositoryInterface):
    def __init__(self):
        self.students = {}
        
    def load_from_file(self, path=f"{BASE_DIR}/data/students.json"):
        with open(path, "r", encoding="utf-8") as file:
            students = json.load(file)
            for student in students:
                object_student = Student.from_dict(student)
                self.students[object_student.get_id()] = object_student
                
    def save_to_file(self, path = f"{BASE_DIR}/data/students.json"):
        with open(path, "w", encoding="utf-8") as file:
            students = [student.to_dict() for student in self.students.values()]
            json.dump(students, file, ensure_ascii=False, indent=4)
            
    def save_to_camel_file(self, path = f"{BASE_DIR}/test/test_data/spring/students.json"):
        with open(path, "w", encoding="utf-8") as file:
            students = [student.to_map() for student in self.students.values()]
            json.dump(students, file, ensure_ascii=False, indent=4)
    
    def clear_store(self):
        self.students.clear()
    
    #Implement the methods from the interface
    def get_length(self) -> int:
        return len(self.students)
    
    def get_student(self, student_id: int) -> Student:
        if student_id not in self.students:
            raise KeyError(f"Student with id {student_id} doesn't exist.")
        return self.students[student_id]

    def get_students(self) -> List[Student]:
        return list(self.students.values())

    def create_student(self, student: Student) -> Student:
        if student.get_id() in self.students:
            raise ValueError(f"Student with id {student.get_id()} already exist.")
        self.students[student.get_id()] = student
        return student

    def update_student(self, student: Student) -> Student:
        if student.get_id() not in self.students:
            raise ValueError(f"Student with id {student.get_id()} doesn't exist.")
        self.students[student.get_id()] = student

    def delete_student(self, student_id: int) -> None:
        if student_id not in self.students:
            raise KeyError(f"Cannot delete: no student with id {student_id}")
        del self.students[student_id]

