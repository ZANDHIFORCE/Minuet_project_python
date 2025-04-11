import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from datetime import time
from domain.lesson_slot import LessonSlot
from repository.memory.memory_lesson_slot_repository import MemoryLessonSlotRepository


class TestMemoryLessonSlotRepository(unittest.TestCase):

    def setUp(self):
        self.repo = MemoryLessonSlotRepository()
        self.slot1 = LessonSlot(id=1, student_id=101, teacher_id=201, day=0, time=time(15, 0))
        self.slot2 = LessonSlot(id=2, student_id=102, teacher_id=202, day=2, time=time(16, 0))

    def tearDown(self):
        self.repo.clear_store()
        
    def test_save_load_from_file(self):
        #given
        self.repo.create_lesson_slot(self.slot1)
        self.repo.create_lesson_slot(self.slot2)
        TEST_PATH = f"{BASE_DIR}/test/test_data/test_lesson_slots.json"
        # save
        self.repo.save_to_file(path=TEST_PATH)

        # clear current repo
        self.repo.clear_store()
        self.assertEqual(self.repo.get_length(), 0)

        # load again
        self.repo.load_from_file(path=TEST_PATH)

        # check restored data
        self.assertEqual(self.repo.get_length(), 2)
        restored = self.repo.get_lesson_slot(1)
        self.assertEqual(restored.to_dict(), self.slot1.to_dict())
        
        # os.remove(TEST_PATH)
        
    def test_snake_to_cmel_json(self):
        self.repo.load_from_file(
            path = f"{BASE_DIR}/data/lesson_slots.json"
        )
        self.repo.save_to_camel_file(
            path = f"{BASE_DIR}/test/test_data/spring/lessonSlots.json"
        )

    def test_create_and_get_lesson_slot(self):
        self.repo.create_lesson_slot(self.slot1)
        result = self.repo.get_lesson_slot(1)
        self.assertEqual(result.to_dict(), self.slot1.to_dict())

    def test_get_length(self):
        self.repo.create_lesson_slot(self.slot1)
        self.repo.create_lesson_slot(self.slot2)
        self.assertEqual(self.repo.get_length(), 2)

    def test_get_lesson_slots(self):
        self.repo.create_lesson_slot(self.slot1)
        self.repo.create_lesson_slot(self.slot2)
        all_slots = self.repo.get_lesson_slots()
        self.assertEqual(len(all_slots), 2)

    def test_update_lesson_slot(self):
        self.repo.create_lesson_slot(self.slot1)
        updated = LessonSlot(id=1, student_id=999, teacher_id=888, day=3, time=time(10, 30))
        self.repo.update_lesson_slot(updated)
        result = self.repo.get_lesson_slot(1)
        self.assertEqual(result.to_dict(), updated.to_dict())

    def test_delete_lesson_slot(self):
        self.repo.create_lesson_slot(self.slot1)
        self.repo.delete_lesson_slot(1)
        self.assertEqual(self.repo.get_length(), 0)

    def test_clear_store(self):
        self.repo.create_lesson_slot(self.slot1)
        self.repo.create_lesson_slot(self.slot2)
        self.repo.clear_store()
        self.assertEqual(self.repo.get_length(), 0)

if __name__ == '__main__':
    unittest.main()
