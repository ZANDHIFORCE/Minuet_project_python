import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from repository.interface.lesson_info_repository_interface import LessonInfoRepositoryInterface
from domain.lesson_info import LessonInfo
from typing import List
import json

class MemoryLessonInfoRepository(LessonInfoRepositoryInterface):
    def __init__(self):
        self.lessons = {}
        
    def load_from_file(self, path = f"{BASE_DIR}/data/lessons_info.json"):
        with open(path,"r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                lesson_info = LessonInfo.from_dict(item)
                self.lessons[lesson_info.get_id()] = lesson_info
    
    def save_to_file(self, path = f"{BASE_DIR}/data/lessons_info.json"):
        with open(path, "w", encoding="utf-8") as file:
            data = [ lessons_info.to_dict() for lessons_info in self.lessons.values()]
            json.dump(data,file,ensure_ascii=False, indent=4)
    
    def clear_store(self):
        self.lessons.clear()
        
    #Implement the methods from the interface
    def get_length(self) -> int:
        return len(self.lessons)

    def get_lesson_info(self, lesson_info_id: int) -> LessonInfo:
        if lesson_info_id not in self.lessons:
            raise KeyError(f"Cannot be found: lesson_info_id:{lesson_info_id}")
        return self.lessons[lesson_info_id]
            
    def get_lessons_info(self) -> List[LessonInfo]:
        return list(self.lessons.values())

    def create_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        if lesson_info.get_id() in self.lessons:
            raise ValueError(f"Already existed in lessons: ID({lesson_info.get_id()})")
        self.lessons[lesson_info.get_id()]=lesson_info

    def update_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        if lesson_info.get_id() not in self.lessons:
            raise ValueError(f"not exist in lessons: lesson_info(ID: {lesson_info.get_id()})")
        self.lessons[lesson_info.get_id()] = lesson_info

    def delete_lesson_info(self, lesson_info_id: int) -> None:
        if lesson_info_id not in self.lessons:
            raise KeyError(f"not exist in lessons: lesson_info_id({lesson_info_id})")
        del self.lessons[lesson_info_id]