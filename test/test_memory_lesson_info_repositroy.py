import os, sys, unittest, json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from typing import List
from repository.memory.memory_lesson_info_repository import MemoryLessonInfoRepository
from domain.lesson_info import LessonInfo
from datetime import datetime

class TestMemoryLessonSlotRepository(unittest.TestCase):
    def setUp(self):
        self.lesson_info_repositroy = MemoryLessonInfoRepository()
        
    def tearDown(self):
        self.lesson_info_repositroy.clear_store()
    
    def test_save_load(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False
        )
        lesson_info_2 = LessonInfo(
            lesson_id=2,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,2),
            completed=False
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        self.lesson_info_repositroy.create_lesson_info(lesson_info_2)
        pathname = f"{BASE_DIR}/test/test_data/test_lesson_infos.json"
        #when
        self.lesson_info_repositroy.save_to_file(
            path = pathname
        )
        self.lesson_info_repositroy.load_from_file(
            path = pathname
        )
        #then
        for lesson_info in self.lesson_info_repositroy.get_lesson_infos():
            if lesson_info_1.get_id() == lesson_info.get_id():
                self.assertEqual(lesson_info_1.to_dict(), lesson_info.to_dict())
            else:
                self.assertEqual(lesson_info_2.to_dict(), lesson_info.to_dict())
                
        # os.remove(pathname)
        
    def test_snake_to_camel_json(self):
        self.lesson_info_repositroy.load_from_file(
            path = f"{BASE_DIR}/data/lesson_infos.json"
        )
        self.lesson_info_repositroy.save_to_camel_file(
            path = f"{BASE_DIR}/test/test_data/spring/lessonInfos.json"
        )

    
    #Implement the methods from the interface
    def test_get_length(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        lesson_info_2 = LessonInfo(
            lesson_id=2,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,2),
            completed=False,
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        self.lesson_info_repositroy.create_lesson_info(lesson_info_2)
        #when
        length = self.lesson_info_repositroy.get_length()
        #then
        self.assertEqual(length, 2)
        
    def test_get_lesson_info(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        #when
        lesson_info_2 = self.lesson_info_repositroy.get_lesson_info(1)
        #then
        self.assertEqual(lesson_info_1.to_dict(), lesson_info_2.to_dict())
        

    def test_get_lesson_infos(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        lesson_info_2 = LessonInfo(
            lesson_id=2,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,2),
            completed=False,
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        self.lesson_info_repositroy.create_lesson_info(lesson_info_2)
        #when
        lesson_infos = self.lesson_info_repositroy.get_lesson_infos()
        #then
        for lesson_info in lesson_infos:
            if lesson_info.get_id() == lesson_info_1.get_id():
                self.assertEqual(lesson_info.to_dict(), lesson_info_1.to_dict())
            else:
                self.assertEqual(lesson_info.to_dict(), lesson_info_2.to_dict())

    def test_create_lesson_info(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        #when
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        #then
        lesson_info_2 = self.lesson_info_repositroy.get_lesson_info(1)
        self.assertEqual(lesson_info_1.to_dict(), lesson_info_2.to_dict())

    def test_update_lesson_info(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        lesson_info_2 = LessonInfo(
            lesson_id=1,
            teacher_id=3,
            student_id=4,
            datetime=datetime(2025,4,2),
            completed=False,
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        #when
        self.lesson_info_repositroy.update_lesson_info(lesson_info_2)
        #then
        self.assertEqual(self.lesson_info_repositroy.get_lesson_info(1).to_dict(), lesson_info_2.to_dict())

    def test_delete_lesson_info(self):
        #given
        lesson_info_1 = LessonInfo(
            lesson_id=1,
            teacher_id=1,
            student_id=1,
            datetime=datetime(2025,4,1),
            completed=False,
        )
        self.lesson_info_repositroy.create_lesson_info(lesson_info_1)
        #when
        self.lesson_info_repositroy.delete_lesson_info(1)
        #then
        self.assertEqual(self.lesson_info_repositroy.get_length(),0)
        
if __name__ == '__main__':
    unittest.main()