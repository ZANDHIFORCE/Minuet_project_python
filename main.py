import json
from datetime import datetime
from domain.teacher import Teacher
from domain.student import Student
from domain.lesson import Lesson


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
        
    def to_student_dic():
        # {
        # "id": 1,
        # "name": "장예진",
        # "total_sessions": 8,
        # "progress_sessions": 5
        # }
        return {
            "id": self.id,
            "name": self.name,
            "total_sessions": self.total_sessions,
            "progress_sessions": self.progress,
        }
        
    

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
#         },
#         {
#             "date": "2025-03-17",
#             "day": "월",
#             "teacher": "미서T",
#             "time": "17:00"
#         },
#         {
#             "date": "2025-03-24",
#             "day": "월",
#             "teacher": "미서T",
#             "time": "18:00"
#         },
#         {
#             "date": "2025-03-31",
#             "day": "월",
#             "teacher": "미서T",
#             "time": "15:00"
#         },
#         {
#             "date": "2025-03-06",
#             "day": "목",
#             "teacher": "미서T",
#             "time": "15:00"
#         },
#         {
#             "date": "2025-03-13",
#             "day": "목",
#             "teacher": "미서T",
#             "time": "16:00"
#         },
#         {
#             "date": "2025-03-20",
#             "day": "목",
#             "teacher": "미서T",
#             "time": "17:00"
#         },
#         {
#             "date": "2025-03-27",
#             "day": "목",
#             "teacher": "미서T",
#             "time": "18:00"
#         }
#     ]
# },

def main():
    
    print("미뉴엣 첫 시작"),
    teacher_name_list = []
    
    #이전 객체 추출출
    pStudent_list = []
    file_path = "./data/minuet_students_full_schedule_2025_updated.json"
    load_data_from_json(file_path, pStudent_list)
    print(f"총 {len(pStudent_list)}명")
    for pStudent in pStudent_list:
        for lesson in pStudent.lesson_plan:
            if  lesson.teacher.rstrip("T") not in teacher_name_list:
                teacher_name_list.append(lesson.teacher.rstrip("T"))
    
    
    #학생 객체 추출
    student_list =[]
    for student in pStudent_list:
        student_list.append({"id": student.id, "student": Student(student.name, student.progress, student.total_sessions, student.id)})
        print(student.name)
    
    
    #선생 객체 추출
    teacher_list = []
    teacher_id = 1
    for teacherName in teacher_name_list:
        teacher_list.append({"id": teacher_id, "teacher": Teacher(teacherName,"piano", teacher_id)})
        teacher_id += 1
        print(teacherName)
    
    #레슨 객체 추출
    lesson_list = []
    lesson_id = 1
    for pStudent in pStudent_list:
        for lesson in pStudent.lesson_plan:
            # lesson_id: Any, teacher_id: Any, student_id: Any, lesson_datetime: Any) -> Schedule
            lesson_id
            
            teacher_id = 0
            for item in teacher_list:
                if item["teacher"].name == lesson.teacher.rstrip("T"):
                    teacher_id = item["id"]
                    break
            # for id , teacher in teacher_list:
            #     if teacher.name in lesson.teacher:
            #         teacher_id = id
            #         break
                
            student_id = 0
            for item in student_list:
                if item["student"].name == pStudent.name:
                    student_id = item["id"]
                    break
            
            # "2025-03-27" + "18:00"
            lesson_datetime = datetime.strptime(f"{lesson.date} {lesson.time}", "%Y-%m-%d %H:%M")
            
            lesson_list.append(Lesson(lesson_id, teacher_id, student_id, lesson_datetime))    
            
            lesson_id += 1
            print(lesson_id, teacher_id, student_id, lesson_datetime)
    
    students = [ item["student"] for item in student_list]
    teachers = [ item["teacher"] for item in teacher_list]
    lessons = lesson_list
    
    save_data_to_jsons(students, teachers, lessons)
    
    
    
def load_data_from_json(file_path, student_list):
    
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
        student_list.append(PostStudent(id, name, schedules, total_sessions, progress_sessions, lesson_plan))
        id += 1
        
def save_data_to_jsons(students, teachers, lessons):
    students_data = [student.to_dict() for student in students]
    with open("./data/students.json", "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=4)
    teacher_date = [teacher.to_dict() for teacher in teachers]
    with open("./data/teachers.json","w",encoding="utf-8") as f:
        json.dump(teacher_date, f, ensure_ascii=False, indent=4)
        
    lesson_date = [lesson.to_dict() for lesson in lessons]
    with open("./data/lessons.json","w",encoding="utf-8") as f:
        json.dump(lesson_date, f, ensure_ascii=False, indent=4)
    
if __name__ == "__main__":
    main()