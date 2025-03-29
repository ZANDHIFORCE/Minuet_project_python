from abc import ABC, abstractmethod
from domain.teacher import Teacher
from typing import List


class TeacherRepositoryInterface(ABC):
    @abstractmethod
    def get_length(self) -> int:
        pass
    
    @abstractmethod
    def get_teacher(self, teacher_id: int) -> Teacher:
        pass

    @abstractmethod
    def get_teachers(self) -> List[Teacher]:
        pass

    @abstractmethod
    def create_teacher(self, teacher: Teacher) -> Teacher:
        pass

    @abstractmethod
    def update_teacher(self, teacher: Teacher) -> Teacher:
        pass

    @abstractmethod
    def delete_teacher(self, teacher_id: int) -> None:
        pass