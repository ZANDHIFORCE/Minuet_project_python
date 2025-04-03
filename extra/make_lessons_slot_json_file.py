import sys
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from repository.memory.memory_student_repository import MemoryStudentRepository
from repository.memory.memory_teacher_repository import MemoryTeacherRepository
from repository.memory.memory_lesson_info_repository import MemoryLessonInfoRepository
from datetime import datetime
from datetime import time
from domain.lesson_slot import LessonSlot



student_repository = MemoryStudentRepository()
teacher_repository = MemoryTeacherRepository()
lesson_repository = MemoryLessonInfoRepository()

student_repository.load_from_file()
teacher_repository.load_from_file()
lesson_repository.load_from_file()


print(student_repository.get_length())
print(teacher_repository.get_length())
print(lesson_repository.get_length())



start_date = datetime(2025,3,3)
end_date = datetime(2025,3,10)
count = 0
korean_weekday = ['월', '화', '수', '목', '금', '토', '일']

lesson_slots = {}

#{'id': 1, 'teacher_id': 1, 'student_id': 1, 'datetime': '2025-03-03T15:00'}
lesson_slots = {}
slot_id = 1
for lesson_info in lesson_repository.get_lessons_info():
    if start_date <= lesson_info.get_datetime() < end_date:
        print(lesson_info.get_datetime().time())
        lesson_slot = LessonSlot(
            slot_id, 
            lesson_info.get_student_id(), 
            lesson_info.get_teacher_id(), 
            lesson_info.get_datetime().weekday(), 
            lesson_info.get_datetime().time()
        )
        lesson_slots[slot_id] = lesson_slot
        print(slot_id)
        slot_id+=1
        
with open(f"{BASE_DIR}/test/test_data/lesson_slots.json","w",encoding="utf-8") as file:
    data = [lesson_slot.to_dict() for lesson_slot in lesson_slots.values()]
    json.dump(data, file,indent=4,ensure_ascii=False)
        
        
        
print(count)
