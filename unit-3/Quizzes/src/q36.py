class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def get_name(self):
        if not isinstance(self.name,str):
            raise ValueError("Name must be a string")
        return self.name
    def get_age(self):
        if not isinstance(self.age, int):
            raise ValueError("Please enter a whole number")
        return self.age

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
        self.name=name
        self.age=age
    def get_grade(self):
        return self.grade

class Classroom:
    def __init__(self):
        self.students=[]

    def add_students(self,student):
        self.students.append(student)

    def remove_students(self,student):
        if student not in self.students:
            raise ValueError("Student not in classroom. Please enter a valid student.")
        self.students.remove(student)

    def average_score(self):
        if len(self.students)==0:
            raise ValueError("Classroom is empty")
        avg_grade=0
        for j in self.students:
            avg_grade+=j.get_grade()
        avg_grade/=len(self.students)
        return avg_grade