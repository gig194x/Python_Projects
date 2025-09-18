# Student Grades Management System Code 
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}  # {course: grade}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Avg: {self.get_average():.2f}"


class GradeSystem:
    def __init__(self):
        self.students = {}  # {id: Student}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")
        else:
            print("Student already exists.")

    def add_grade(self, student_id, course, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(course, grade)
            print(f"Grade {grade} added for {self.students[student_id].name} in {course}.")
        else:
            print("Student not found!")

    def show_all_students(self):
        for student in self.students.values():
            print(student)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.get_average())


# -------- Example Run ----------
if __name__ == "__main__":
    system = GradeSystem()

    system.add_student(1, "Ali")
    system.add_student(2, "Sara")

    system.add_grade(1, "Math", 90)
    system.add_grade(1, "Physics", 80)
    system.add_grade(2, "Math", 95)

    print("\nAll Students:")
    system.show_all_students()

    print("\nTop Student:")
    print(system.top_student())
