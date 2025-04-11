import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from repository.interface.lesson_info_repository_interface import LessonInfoRepositoryInterface
from domain.lesson_info import LessonInfo
from typing import List
import json

class MemoryLessonInfoRepository(LessonInfoRepositoryInterface):
    def __init__(self):
        self.lesson_infos = {}
        
    def load_from_file(self, path = f"{BASE_DIR}/data/lesson_infos.json"):
        with open(path,"r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                lesson_info = LessonInfo.from_dict(item)
                self.lesson_infos[lesson_info.get_id()] = lesson_info
    
    def save_to_file(self, path = f"{BASE_DIR}/data/lesson_infos.json"):
        with open(path, "w", encoding="utf-8") as file:
            data = [ lesson_info.to_dict() for lesson_info in self.lesson_infos.values()]
            json.dump(data,file,ensure_ascii=False, indent=4)
    
    def save_to_camel_file(self, path = f"{BASE_DIR}/test/test_data/lesson_infos.json"):
        with open(path, "w", encoding="utf-8") as file:
            data = [ lesson_info.to_map() for lesson_info in self.lesson_infos.values()]
            json.dump(data,file,ensure_ascii=False, indent=4)
    
    def clear_store(self):
        self.lesson_infos.clear()
        
    #Implement the methods from the interface
    def get_length(self) -> int:
        return len(self.lesson_infos)

    def get_lesson_info(self, lesson_info_id: int) -> LessonInfo:
        if lesson_info_id not in self.lesson_infos:
            raise KeyError(f"Cannot be found: lesson_info_id:{lesson_info_id}")
        return self.lesson_infos[lesson_info_id]
            
    def get_lesson_infos(self) -> List[LessonInfo]:
        return list(self.lesson_infos.values())

    def create_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        if lesson_info.get_id() in self.lesson_infos:
            raise ValueError(f"Already existed in lesson_infos: ID({lesson_info.get_id()})")
        self.lesson_infos[lesson_info.get_id()]=lesson_info

    def update_lesson_info(self, lesson_info: LessonInfo) -> LessonInfo:
        if lesson_info.get_id() not in self.lesson_infos:
            raise ValueError(f"not exist in lesson_infos: lesson_info(ID: {lesson_info.get_id()})")
        self.lesson_infos[lesson_info.get_id()] = lesson_info

    def delete_lesson_info(self, lesson_info_id: int) -> None:
        if lesson_info_id not in self.lesson_infos:
            raise KeyError(f"not exist in lesson_infos: lesson_info_id({lesson_info_id})")
        del self.lesson_infos[lesson_info_id]