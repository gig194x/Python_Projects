# =====================
# Student Class with Encapsulation
# =====================
class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id   # private
        self.__name = name               # private
        self.__grades = {}               

    # Getters
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_grades(self):
        return self.__grades.copy()  # return copy for safety

    # Add grade
    def add_grade(self, course, grade):
        self.__grades[course] = grade

    # GPA calculation
    def get_gpa(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, GPA: {self.get_gpa():.2f}"


# =====================
# Grade Management System
# =====================
class GradeSystem:
    def __init__(self):
        self.__students = {}  # private {id: Student}

    # Add student
    def add_student(self, student_id, name):
        if student_id not in self.__students:
            self.__students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")
        else:
            print("Student already exists.")

    # Add grade
    def add_grade(self, student_id, course, grade):
        if student_id in self.__students:
            self.__students[student_id].add_grade(course, grade)
            print(f"Grade {grade} added for {self.__students[student_id].get_name()} in {course}.")
        else:
            print("Student not found!")

    # Merge Sort by GPA
    def merge_sort_students(self, student_list):
        if len(student_list) <= 1:
            return student_list
        mid = len(student_list) // 2
        left = self.merge_sort_students(student_list[:mid])
        right = self.merge_sort_students(student_list[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].get_gpa() >= right[j].get_gpa():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Show sorted students
    def show_all_students_sorted(self):
        student_list = list(self.__students.values())
        sorted_students = self.merge_sort_students(student_list)
        print("\n--- Students Sorted by GPA ---")
        for student in sorted_students:
            print(student)

    # Top student
    def top_student(self):
        if not self.__students:
            return None
        sorted_students = self.merge_sort_students(list(self.__students.values()))
        return sorted_students[0]


# =====================
# Interactive Menu
# =====================
def main():
    system = GradeSystem()

    while True:
        print("\n==== Student Grades Management System ====")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Show All Students Sorted by GPA")
        print("4. Show Top Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            system.add_student(student_id, name)

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            course = input("Enter Course Name: ")
            grade = float(input("Enter Grade: "))
            system.add_grade(student_id, course, grade)

        elif choice == "3":
            system.show_all_students_sorted()

        elif choice == "4":
            top = system.top_student()
            if top:
                print("\nTop Student:")
                print(top)
            else:
                print("No students in the system.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
