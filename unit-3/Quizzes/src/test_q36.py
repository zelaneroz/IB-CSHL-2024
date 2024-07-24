import pytest
from q36 import Student,Classroom,Person

def test_person():
    p1=Person("Antonia",16)
    assert p1.get_name()=="Antonia"
    assert p1.get_age()==16
    with pytest.raises(ValueError):
        p2 = Person(17,"Zelan")
        p2.get_age()
        p2.get_name()
def test_student():
    student=Student("Sahana",17,85)
    assert student.get_grade() == 85
    assert student.get_name() == "Sahana"
    assert student.get_age() == 17
    with pytest.raises(ValueError):
        student = Student(["Yasmina"],17,90)
        student.get_name()

def test_classroom():
    c = Classroom()
    s1 = Student("Mayte", 17,95)
    s2 = Student("Lemie", 17, 84)
    s3 = Student("Sana", 17, 87)
    c.add_students(s1)
    c.add_students(s2)
    c.add_students(s3)
    c.remove_students(s2)
    assert c.average_score() == 91
    c.remove_students(s1)
    c.remove_students(s3)
    with pytest.raises(ValueError):
        c.average_score()
