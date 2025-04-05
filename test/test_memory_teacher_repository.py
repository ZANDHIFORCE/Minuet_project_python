import os, sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from repository.memory.memory_teacher_repository import MemoryTeacherRepository
from domain.teacher import Teacher

class TestMemoryTeacherRepository(unittest.TestCase):
    def setUp(self):
        self.repository = MemoryTeacherRepository()
    
    def tearDown(self):
        self.repository.clear_store()
        
    def test_load_save_file(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        teacher2 = Teacher("동휘", "computer", 2)
        self.repository.create_teacher(teacher1)
        self.repository.create_teacher(teacher2)
        #when
        self.repository.save_to_file(f"{BASE_DIR}/test/test_data/teachers.json")
        self.repository.clear_store()
        self.repository.load_from_file(f"{BASE_DIR}/test/test_data/teachers.json")
        #then
        teachers = self.repository.get_teachers()
        for teacher in teachers:
            if teacher.id == teacher1.id:
                self.assertEqual(teacher1.to_dict(), teacher.to_dict())
            else:
                self.assertEqual(teacher2.to_dict(), teacher.to_dict())
        
    #Implement the methods from the interface  
    def test_get_length(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        #when
        self.repository.create_teacher(teacher1)
        #then
        self.assertEqual(1, self.repository.get_length())
    
    def test_get_teacher(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        self.repository.create_teacher(teacher1)
        #when
        teacher2 = self.repository.get_teacher(1)
        #then
        self.assertEqual(teacher1.to_dict(), teacher2.to_dict())
    
    def test_get_teacher_exception(self):
        #when
        with self.assertRaises(KeyError):
            self.repository.get_teacher(1)
    
    def test_create_teacher(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        #when
        self.repository.create_teacher(teacher1)
        #then
        self.assertEqual(teacher1.to_dict(), self.repository.get_teacher(1).to_dict())
    
    def test_create_teacher_exception(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        teacher2 = Teacher("동휘", "computer", 1)
        self.repository.create_teacher(teacher1)
        #when
        with self.assertRaises(ValueError):
            self.repository.create_teacher(teacher2)

    def test_update_teacher(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        teacher2 = Teacher("미서", "computer", 1)
        self.repository.create_teacher(teacher1)
        #when
        self.repository.update_teacher(teacher2)
        #then
        self.assertEqual(teacher2.to_dict(), self.repository.get_teacher(1).to_dict())
    
    def test_update_teacher_exception(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        #when
        with self.assertRaises(ValueError):
            self.repository.update_teacher(teacher1)
        #then

    def test_delete_teacher(self):
        #given
        teacher1 = Teacher("미서", "piano", 1)
        self.repository.create_teacher(teacher1)
        #when
        self.repository.delete_teacher(1)
        #then
        self.assertEqual(self.repository.get_length(), 0)
    
    def test_delete_teacher_exception(self):
        #given
        #when
        with self.assertRaises(KeyError):
            self.repository.delete_teacher(1)
        #then
    
if __name__ == '__main__':
    unittest.main()