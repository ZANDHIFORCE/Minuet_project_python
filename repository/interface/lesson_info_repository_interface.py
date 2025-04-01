from abc import ABC, abstractmethod
from domain.lesson_info import LessonInfo
from typing import List


class LessonInfoRepositoryInterface(ABC):
    
    @abstractmethod
    def get_length(self) -> int:
        pass
    
    @abstractmethod
    def get_lesson_info(self, lesson_info_id: int) -> LessonInfo:
        pass

    @abstractmethod
    def get_lessons_info(self) -> List[LessonInfo]:
        pass

    @abstractmethod
    def create_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        pass

    @abstractmethod
    def update_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        pass

    @abstractmethod
    def delete_lesson_info(self, lesson_info_id: int) -> None:
        pass