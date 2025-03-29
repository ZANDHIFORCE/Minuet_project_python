from abc import ABC, abstractmethod
from domain.lesson_slot import LessonSlot
from typing import List


class LessonPlanRepositoryInterface(ABC):
    @abstractmethod
    def get_length(self) -> int:
        pass
    
    @abstractmethod
    def get_student(self, lesson_slot_id: int) -> LessonSlot:
        pass

    @abstractmethod
    def get_students(self) -> List[LessonSlot]:
        pass

    @abstractmethod
    def create_student(self, lesson_slot: LessonSlot) -> LessonSlot:
        pass

    @abstractmethod
    def update_student(self, lesson_slot: LessonSlot) -> LessonSlot:
        pass

    @abstractmethod
    def delete_student(self, lesson_slot_id: int) -> None:
        pass