from abc import ABC, abstractmethod
from typing import List
from domain.lesson_slot import LessonSlot

class LessonSlotRepositoryInterface(ABC):
    @abstractmethod
    def get_length(self) -> int:
        pass

    @abstractmethod
    def get_lesson_slot(self, lesson_slot_id: int) -> LessonSlot:
        pass

    @abstractmethod
    def get_lesson_slots(self) -> List[LessonSlot]:
        pass

    @abstractmethod
    def create_lesson_slot(self, lesson_slot: LessonSlot) -> LessonSlot:
        pass

    @abstractmethod
    def update_lesson_slot(self, lesson_slot: LessonSlot) -> LessonSlot:
        pass

    @abstractmethod
    def delete_lesson_slot(self, lesson_slot_id: int) -> None:
        pass

    @abstractmethod
    def clear_store(self) -> None:
        pass
    