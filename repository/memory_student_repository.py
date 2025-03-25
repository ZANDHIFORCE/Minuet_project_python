from repository.student_repository_interface import StudentRepositoryInterface
from domain.student import Student
from typing import List

class MemoryStudentRepository(StudentRepositoryInterface):
    def __init__(self):
        self.students = {}
        
        def load_from_file(self):
            pass
        
        def save_to_file(self):
            pass
        
        def get_student(self, student_id: int) -> Student:
            pass

        def get_students(self) -> List[Student]:
            pass

        def create_student(self, student: Student) -> Student:
            pass

        def update_student(self, student: Student) -> Student:
            pass

        def delete_student(self, student_id: int) -> None:
            pass

