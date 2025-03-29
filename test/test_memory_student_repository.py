import os, sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from repository.memory.memory_student_repository import MemoryStudentRepository 
from domain.student import Student

class TestMemoryStudentRepository(unittest.TestCase):
    def setUp(self):
        self.repository = MemoryStudentRepository()

    def tearDown(self):
        self.repository.clearStore()

    def test_save_load(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        self.repository.students[1]= student1
        student2 = Student("송미서", 4, 12, 2)
        self.repository.students[2] = student2
        #when
        self.repository.save_to_file(f"{BASE_DIR}/test/test_data/test_students.json")
        self.repository.clearStore()
        self.repository.load_from_file(f"{BASE_DIR}/test/test_data/test_students.json")
        #then
        self.assertEqual(student1.to_dict(), self.repository.students[1].to_dict())
        self.assertEqual(student2.to_dict(), self.repository.students[2].to_dict())
    
    def test_get_length(self):
        #given
        self.repository.create_student(Student("조동휘", 5, 12, 1))
        #when
        length = self.repository.get_length()
        #then
        self.assertEqual(1, length)
        
    def test_get_student(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        #when
        self.repository.students[1]= student1
        #then
        self.assertEqual(self.repository.get_student(1).to_dict(), student1.to_dict())
        
    def test_get_student_exception(self):
        #given
        #when
        with self.assertRaises(KeyError):
            self.repository.get_student(1)
        #then

    def test_get_students(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        self.repository.students[1]= student1
        student2 = Student("송미서", 4, 12, 2)
        self.repository.students[2] = student2
        #when
        students = self.repository.get_students()
        #then
        for student in students:
            if student.id == student1.id:
                self.assertEqual(student.to_dict(), student1.to_dict())
            else:
                self.assertEqual(student.to_dict(), student2.to_dict())

    def test_create_student(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        #when
        student2 = self.repository.create_student(student1)
        #then
        self.assertEqual(student1.to_dict(), student2.to_dict())
        
    def test_create_student_exception(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        student2 = Student("송미서", 4, 12, 1)
        #when
        self.repository.create_student(student1)
        with self.assertRaises(ValueError):
            self.repository.create_student(student2)

    def test_update_student(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        student2 = Student("조동휘", 6, 12, 1)
        self.repository.create_student(student1)
        #when
        self.repository.update_student(student2)
        #then
        for student in self.repository.get_students():
            self.assertEqual(student.to_dict(), student2.to_dict())

    def test_update_student_exception(self):
        #given
        student1 = Student("조동휘", 5, 12, 1)
        #when
        with self.assertRaises(ValueError):
            self.repository.update_student(student1)
        #then
    
    def test_delete_student(self):
        #given
        self.repository.create_student(Student("조동휘", 5, 12, 1))
        #when
        self.repository.delete_student(1)
        #then
        self.assertEqual(len(self.repository.students), 0)
        
    def test_delete_student_exception(self):
        #given
        #when
        with self.assertRaises(KeyError):
            self.repository.delete_student(1)
        #then

if __name__ == '__main__':
    unittest.main()