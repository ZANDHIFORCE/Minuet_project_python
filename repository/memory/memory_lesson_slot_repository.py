import os, sys, json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from typing import List
from domain.lesson_slot import LessonSlot
from repository.interface.lessons_slot_repository_interface import LessonSlotRepositoryInterface
from datetime import time, datetime
class MemoryLessonSlotRepository(LessonSlotRepositoryInterface):
    def __init__(self):
        self.lesson_slots = {}
        
    def load_from_file(self, path=f"{BASE_DIR}/data/lesson_slots.json"):
        with open(path, "r", encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                lesson_slot = LessonSlot.from_dict(item)
                self.create_lesson_slot(lesson_slot)
    
    def save_to_file(self, path=f"{BASE_DIR}/data/lesson_slots.json"):
        with open(path,"w",encoding="utf-8") as file:
            data = [lesson_slot.to_dict() for lesson_slot in self.lesson_slots.values()]
            json.dump(data, file, indent=4, ensure_ascii=False)
        
    #Implementation    
    def get_length(self) -> int:
        return len(self.lesson_slots)

    def get_lesson_slot(self, lesson_slot_id: int) -> LessonSlot:
        if lesson_slot_id not in self.lesson_slots:
            raise KeyError("해당 아이디가 lessons_slots에 없다")
        return self.lesson_slots[lesson_slot_id]

    def get_lesson_slots(self) -> List[LessonSlot]:
        return list(self.lesson_slots.values())

    def create_lesson_slot(self, lesson_slot: LessonSlot) -> LessonSlot:
        if lesson_slot.get_id() in self.lesson_slots:
            raise ValueError("이미 해당 객체 아이디가 lessons_slots에 있습니다.")
        self.lesson_slots[lesson_slot.get_id()] = lesson_slot
        
    def update_lesson_slot(self, lesson_slot: LessonSlot) -> LessonSlot:
        if lesson_slot.get_id() not in self.lesson_slots:
            raise ValueError("헤당 객체 아이디가 존재 하지 않습니다.: lessons_slots")
        self.lesson_slots[lesson_slot.get_id()] = lesson_slot
        
    def delete_lesson_slot(self, lesson_slot_id: int) -> None:
        if lesson_slot_id not in self.lesson_slots:
            raise KeyError("헤당 아이디가 존재 하지 않습니다.: lessons_slots")
        del self.lesson_slots[lesson_slot_id]
        
    def clear_store(self) -> None:
        self.lesson_slots.clear()