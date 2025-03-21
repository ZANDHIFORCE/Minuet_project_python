import json


class PostDefaultSchedule:
    def __init__(self, day, teacher):
        self.day = day
        self.teacher = teacher

class PostStudent:
    def __init__(self, name, schedule, total_sessions, progress, lesson_plan):
        self.name = name
        self.schedule = schedule
        self.total_sessions = total_sessions
        self.progress = progress
        self.lesson_plan = lesson_plan
        
class PostTeacher:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
    

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
    student_list = []
    file_path = "./data/minuet_students_full_schedule_2025_updated.json"
    loadData(file_path, student_list)
    print(f"총 {len(student_list)}명")
    for student in student_list:
        print(student.name)
        
    
    print()
    saveData()
    
    
def loadData(file_path, student_list):
    
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
        student_list.append(PostStudent(name, schedules, total_sessions, progress_sessions, lesson_plan))
        
def saveData():
    print("데이터 저장")
    
if __name__ == "__main__":
    main()