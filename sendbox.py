import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from datetime import datetime

from domain.teacher import Teacher
from domain.student import Student
from domain.lesson_info import LessonInfo
from domain.lesson_slot import LessonSlot

from repository.memory.memory_teacher_repository import MemoryTeacherRepository
from repository.memory.memory_student_repository import MemoryStudentRepository
from repository.memory.memory_lesson_info_repository import MemoryLessonInfoRepository
from repository.memory.memory_lesson_slot_repository import MemoryLessonSlotRepository

teacher_repo = MemoryTeacherRepository()
student_repo = MemoryStudentRepository()
lesson_info_repo = MemoryLessonInfoRepository()
lesson_slot_repo = MemoryLessonSlotRepository()

teacher_repo.load_from_file()
student_repo.load_from_file()
lesson_info_repo.load_from_file()
lesson_slot_repo.load_from_file()

korean_weekday = ["월","화","수","목","금","토","일"]

student_id = 1
student = student_repo.get_student(student_id)
#{'id': 1, 'name': '홍서율', 'total_sessions': 8, 'progress_sessions': 5}

lesson_info_list = lesson_info_repo.get_lessons_info()
lesson_info_list.sort(key=lambda lesson: lesson.datetime)
print(f"아래는 {student.get_name()}학생에게 예정되어있는 레슨입니다.")
for lesson_info in lesson_info_list:
    if lesson_info.get_student_id()==student_id:
        lessons_datetime = lesson_info.datetime
        weekday = korean_weekday[lessons_datetime.weekday()]
        datatime_str= lessons_datetime.strftime(f"%m/%d({weekday}) %H:%M")
        teacher = teacher_repo.get_teacher(lesson_info.get_teacher_id())
        print(f"{datatime_str} {teacher.get_name()}선생님 {teacher.get_subject()} 레슨")

