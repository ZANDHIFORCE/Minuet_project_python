import json
from datetime import datetime
from domain.teacher import Teacher
from domain.student import Student
from domain.lesson_info import LessonInfo
from repository.memory_student_repository import MemoryStudentRepository

def main():
   repository = MemoryStudentRepository()
   repository.load_from_file()
   repository.save_to_file()
    
if __name__ == "__main__":
    main()