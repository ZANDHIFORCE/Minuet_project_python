from abc import ABC, abstractmethod
from domain.student import Student
from typing import List


class StudentRepositoryInterface(ABC):
    @abstractmethod
    def get_student(self, student_id: int) -> Student:
        pass

    @abstractmethod
    def get_students(self) -> List[Student]:
        pass

    @abstractmethod
    def create_student(self, student: Student) -> Student:
        pass

    @abstractmethod
    def update_student(self, student: Student) -> Student:
        pass

    @abstractmethod
    def delete_student(self, student_id: int) -> None:
        pass