import json
from datetime import datetime
from domain.teacher import Teacher
from domain.student import Student
from domain.lesson_info import LessonInfo


class PostDefaultSchedule:
    def __init__(self, day, teacher):
        self.day = day
        self.teacher = teacher

class PostStudent:
    def __init__(self, id, name, schedule, total_sessions, progress, lesson_plan):
        self.id = id
        self.name = name
        self.schedule = schedule
        self.total_sessions = total_sessions
        self.progress = progress
        self.lesson_plan = lesson_plan
    
class PostLessonInfo:
    def __init__(self, date, day, teacher, time):
        self.date = date
        self.day = day
        self.teacher = teacher
        self.time = time

# {
#     "name": "홍서율",
#     "schedules": [
#         {
#             "day": "월",
#             "teacher": "미서T"
#         },
#         {
#             "day": "목",
#             "teacher": "미서T"
#         }
#     ],
#     "total_sessions": 8,
#     "progress_sessions": 5,
#     "lesson_plan": [
#         {
#             "date": "2025-03-03",
#             "day": "월",
#             "teacher": "미서T",
#             "time": "15:00"
#         },
#         {
#             "date": "2025-03-10",
#             "day": "월",
#             "teacher": "미서T",
#             "time": "16:00"
#         }
#     ]
# },

#


def converter_json_to_jsons(json_file_path, students_path, teachers_path, lessons_path):
    """Json 파일을 읽어서 Student, Teacher, Lesson 객체를 생성하고 json 파일로 저장

    Args:
        json_file_path (str): pStudent json 파일 경로
        students_path (str): 학생들 json 파일 경로
        teachers_path (str): 선생들 json 파일 경로
        lessons_path (str): 레슨들 json 파일 경로
    """
    
    #pStudent_list 불러오기: [PostStudent, PostStudent]
    pStudent_list = load_data_from_json(json_file_path)
    
    students, teachers, lessons = load_class_from_data(pStudent_list)
    
    save_data_to_jsons(students, teachers, lessons, students_path, teachers_path, lessons_path)
    
def load_data_from_json(file_path):
    """Json에서 pStudent리스트 불러오기

    Args:
        file_path (str): json 파일 경로

    Returns:
        List: pStudent 객체 리스트
    """
    
    pStudent_list = []
    
    id = 1
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        name = item["name"]
        schedules = item["schedules"]
        total_sessions = item["total_sessions"]
        progress_sessions = item["progress_sessions"]
        lesson_list = item["lesson_plan"]
        lesson_plan = []
        for lesson in lesson_list:
            date = lesson["date"]
            day = lesson["day"]
            teacher = lesson["teacher"]
            time = lesson["time"]
            lesson_plan.append(PostLessonInfo(date, day, teacher, time))
        pStudent_list.append(PostStudent(id, name, schedules, total_sessions, progress_sessions, lesson_plan))
        id += 1
        
    return pStudent_list

def load_class_from_data(pStudent_list):
    """pStudent 리스트를 불러와서 Student, Teacher, Lesson 객체의 리스트 변환

    Args:
        pStudent_list (List): pStudent 객체 리스트 

    Returns:
        Tuple: (students, teachers, lessons)
    """
    #학생 객체 리스트 생성: [{"id": int, "student": Student}]
    student_list =[]
    for student in pStudent_list:
        student_list.append({"id": student.id, "student": Student(student.name, student.progress, student.total_sessions, student.id)})
    
    #teacher_name_list: [이름, 이름]
    teacher_name_list = []
    for pStudent in pStudent_list:
        for lesson in pStudent.lesson_plan:
            teacher_name = lesson.teacher.rstrip("T")
            if teacher_name not in teacher_name_list:
                teacher_name_list.append(teacher_name)
    
    # 선생님 객체 리스트 생성: [{"id": int, "teacher": Teacher}]
    teacher_list = []
    teacher_id = 1
    for teacherName in teacher_name_list:
        teacher_list.append({"id": teacher_id, "teacher": Teacher(teacherName,"piano", teacher_id)})
        teacher_id += 1
    
    #레슨 객체 생성: [Lesoon, Lesson]
    #Lesson 파라미터
        #lesson_id: Any, 
        #teacher_id: Any, 
        #student_id: Any, 
        #lesson_datetime: Any)
    lesson_list = []
    lesson_id = 1
    for pStudent in pStudent_list:
        for lesson in pStudent.lesson_plan:  
            #teacher_id
            teacher_id = 0
            for item in teacher_list:
                if item["teacher"].name == lesson.teacher.rstrip("T"):
                    teacher_id = item["id"]
                    break
            #student_id
            student_id = 0
            for item in student_list:
                if item["student"].name == pStudent.name:
                    student_id = item["id"]
                    break
            
            #lesson_datetime "2025-03-27" + "18:00"
            lesson_datetime = datetime.strptime(f"{lesson.date}T{lesson.time}", "%Y-%m-%dT%H:%M")
            
            #lesson_list에 lesson 객체 추가 
            lesson_list.append(LessonInfo(lesson_id, teacher_id, student_id, lesson_datetime))    
            lesson_id += 1

    
    students = [ item["student"] for item in student_list]
    teachers = [ item["teacher"] for item in teacher_list]
    lessons = lesson_list
    
    return students, teachers, lessons

def save_data_to_jsons(students, teachers, lessons, students_path, teachers_path, lessons_path):
    """Student, Teacher, Lesson 객체 리스트를 json 파일로 저장

    Args:
        students (List): stduent 객체 리스트 
        teachers (List): teacher 객체 리스트
        lessons (List): lesson 객체 리스트
        students_path (String): 학생 json 파일 경로로
        teachers_path (String): 선생 json 파일 경로로
        lessons_path (String): 레슨 json 파일 경로로
    """
    students_data = [student.to_dict() for student in students]
    with open(students_path, "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=4)
    teacher_date = [teacher.to_dict() for teacher in teachers]
    with open(teachers_path,"w",encoding="utf-8") as f:
        json.dump(teacher_date, f, ensure_ascii=False, indent=4)
    lesson_date = [lesson.to_dict() for lesson in lessons]
    with open(lessons_path,"w",encoding="utf-8") as f:
        json.dump(lesson_date, f, ensure_ascii=False, indent=4)


json_file_path = "./minuet_students_full_schedule_2025_updated.json"
students_path = "./students.json"
teachers_path ="./teachers.json"
lessons_path = "./lessons.json"

converter_json_to_jsons(json_file_path, students_path, teachers_path, lessons_path)