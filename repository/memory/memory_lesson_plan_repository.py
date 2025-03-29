from repository.interface.lesson_plan_repository_interface import LessonPlanRepositoryInterface
from domain.lesson_plan import LessonPlan
from typing import List

class MemoryLesoonSlotRepository(LessonPlanRepositoryInterface):
    def __init__(self):
        self.LesoonSlots = {}
        
    def load_from_file(self, path = ""):
        pass
    
    def save_to_file(self, path = ""):
        pass
    
    
    
    #Implement the methods from the interface
    def get_length(self) -> int:
        return len(self.LesoonSlots)

    def get_student(self, lesson_slot_id: int) -> LessonPlan:
        pass

    def get_students(self) -> List[LessonPlan]:
        pass

    def create_student(self, lesson_slot: LessonPlan) -> LessonPlan:
        pass

    def update_student(self, lesson_slot: LessonPlan) -> LessonPlan:
        pass

    def delete_student(self, lesson_slot_id: int) -> None:
        pass