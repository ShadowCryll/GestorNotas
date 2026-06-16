# =======================================================
# CLASSES (Object-Oriented Programming Re-architecture)
# =======================================================

class Course:
    """Represents an academic course with a name and a grade."""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Student:
    """Represents a student with a name and a list of Course objects."""
    def __init__(self, name):
        self.name = name
        self.courses = []

    def calculate_average(self):
        # Precondition: self.courses may be empty
        # Postcondition: Returns the course grade average or 0.0 if empty
        if not self.courses:
            return 0.0
        return sum(course.grade for course in self.courses) / len(self.courses)


class GradeManager:
    """Manages system data operations, histories (Stack), and review requests (Queue)."""
    def __init__(self):
        self.students = []
        self.action_history = []  # Stack (LIFO)
        self.revision_queue = []   # Queue (FIFO)

    def group_overall_average(self):
        # Precondition: self.students contains valid records
        # Postcondition: Returns the group overall average (average of averages)
        if not self.students:
            return 0.0
        total = sum(student.calculate_average() for student in self.students)
        return total / len(self.students)

    def bubble_sort(self):
        # Precondition: self.students contains valid records
        # Postcondition: Returns a list sorted by average in descending order
        sorted_students = self.students.copy()
        n = len(sorted_students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_students[j].calculate_average() < sorted_students[j + 1].calculate_average():
                    sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
        return sorted_students

    def insertion_sort(self):
        # Precondition: self.students contains valid records
        # Postcondition: Returns a list sorted alphabetically by name
        sorted_students = self.students.copy()
        for i in range(1, len(sorted_students)):
            current = sorted_students[i]
            j = i - 1
            while j >= 0 and sorted_students[j].name.lower() > current.name.lower():
                sorted_students[j + 1] = sorted_students[j]
                j -= 1
            sorted_students[j + 1] = current
        return sorted_students

    def linear_search(self, target_name):
        # Precondition: target_name is a string
        # Postcondition: Returns the Student object if found, otherwise None
        for student in self.students:
            if student.name.lower() == target_name.lower():
                return student
        return None

    def binary_search(self, target_name):
        # Precondition: target_name is a string
        # Postcondition: Sorts internally and returns the Student object if found, otherwise None
        sorted_students = self.insertion_sort()
        low = 0
        high = len(sorted_students) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_students[mid].name.lower() == target_name.lower():
                return sorted_students[mid]
            elif sorted_students[mid].name.lower() < target_name.lower():
                low = mid + 1
            else:
                high = mid - 1
        return None

    def register_student(self):
        name = input("Enter student name: ").strip()

        # Prevent duplicates
        for student in self.students:
            if student.name.lower() == name.lower():
                print("A student with that name already exists.")
                return

        new_student = Student(name)
        for i in range(1, 4):
            course_name = input(f"Enter the name of course {i}: ").strip()
            try:
                grade = float(input(f"Enter the grade for {course_name} (0 to 100): "))
            except ValueError:
                print("You must enter a valid number.")
                return
            if 0 <= grade <= 100:
                new_student.courses.append(Course(course_name, grade))
            else:
                print("Invalid grade. Registration canceled.")
                return

        self.students.append(new_student)
        self.action_history.append(f"Registered student {name}")
        print("Student registered successfully.")

    def display_students_list(self, current_list=None):
        list_to_show = self.students if current_list is None else current_list
        if not list_to_show:
            print("No students registered.")
            return

        for i, student in enumerate(list_to_show, start=1):
            print(f"\n{i}. {student.name}")
            for course in student.courses:
                print(f"   {course.name} - Grade: {course.grade}")
            print(f"   Overall Average: {student.calculate_average():.2f}")

        print(f"\n Group Overall Average: {self.group_overall_average():.2f}")

    def count_passed_failed(self):
        if not self.students:
            print("No students registered.")
            return

        passed = []
        failed = []

        for student in self.students:
            average = student.calculate_average()
            if average >= 60:
                passed.append((student.name, average))
            else:
                failed.append((student.name, average))

        print("\n=== GENERAL RESULTS ===")
        print(f"Passed students: {len(passed)}")
        for name, avg in passed:
            print(f"   {name} - Average: {avg:.2f}")

        print(f"\nFailed students: {len(failed)}")
        for name, avg in failed:
            print(f"   {name} - Average: {avg:.2f}")

        print(f"\n Group Overall Average: {self.group_overall_average():.2f}")

    def update_grade(self):
        name = input("Enter student name: ").strip().lower()
        student = self.linear_search(name)
        
        if student:
            print(f"\nCourses for {student.name}:")
            for i, course in enumerate(student.courses, start=1):
                print(f"{i}. {course.name} - Grade: {course.grade}")

            try:
                index = int(input("Select the course number to update: ")) - 1
                new_grade = float(input("Enter the new grade (0 to 100): "))
            except ValueError:
                print("Invalid input.")
                return

            if 0 <= new_grade <= 100 and 0 <= index < len(student.courses):
                target_course = student.courses[index]
                old_grade = target_course.grade
                target_course.grade = new_grade
                self.action_history.append(f"Updated grade of {target_course.name} for {student.name} from {old_grade} to {new_grade}")
                print("Grade updated successfully.")
            else:
                print("Invalid data.")
            return
        print("Student not found.")

    def delete_course(self):
        name = input("Enter student name: ").strip().lower()
        student = self.linear_search(name)

        if student:
            for i, course in enumerate(student.courses, start=1):
                print(f"{i}. {course.name} - Grade: {course.grade}")

            try:
                index = int(input("Select the course number to delete: ")) - 1
            except ValueError:
                print("Invalid input.")
                return

            if 0 <= index < len(student.courses):
                course_to_delete = student.courses[index].name
                confirm = input(f"Are you sure you want to delete '{course_to_delete}'? (Y/N): ").strip().upper()
                if confirm == "Y":
                    removed = student.courses.pop(index)
                    self.action_history.append(f"Deleted course {removed.name} from {student.name}")
                    print(f" Course '{removed.name}' deleted successfully.")
                else:
                    print("Operation canceled.")
            else:
                print("Invalid index.")
            return
        print("Student not found.")

    def delete_student(self):
        name = input("Enter the name of the student to delete: ").strip().lower()
        for i, student in enumerate(self.students):
            if student.name.lower() == name:
                confirm = input(f"Are you sure you want to completely delete student '{student.name}'? (Y/N): ").strip().upper()
                if confirm == "Y":
                    removed = self.students.pop(i)
                    self.action_history.append(f"Completely deleted student {removed.name}")
                    print(f"Student '{removed.name}' removed from the system.")
                else:
                    print("Operation canceled.")
                return
        print("Student not found.")

    def display_history(self):
        if not self.action_history:
            print("Action history is empty.")
        else:
            print("\n===== ACTION HISTORY (STACK LIFO) =====")
            for action in reversed(self.action_history):
                print("-", action)

    def add_to_revision_queue(self):
        name = input("Enter student name to add to the review queue: ").strip().lower()
        student = self.linear_search(name)
        if student:
            self.revision_queue.append(student)
            print(f"{student.name} was added to the academic review queue.")
            return
        print("Student not found.")

    def process_revision_queue(self):
        if not self.revision_queue:
            print("No students in the review queue.")
        else:
            student = self.revision_queue.pop(0)
            print(f"\nReviewing student: {student.name}")
            for course in student.courses:
                print(f"   {course.name}: {course.grade}")
            print(f"Overall Average: {student.calculate_average():.2f}")


def show_menu():
    print("\n====== ACADEMIC GRADE MANAGER - MILESTONE 06 ======")
    print("1. Register student")
    print("2. Display students")
    print("3. Count passed and failed students")
    print("4. Update grade")
    print("5. Delete course")
    print("6. Delete student")
    print("7. Sort students by average (Bubble Sort)")
    print("8. Sort students alphabetically (Insertion Sort)")
    print("9. Search student (Linear Search)")
    print("10. Search student (Binary Search)")
    print("11. View action history (Stack LIFO)")
    print("12. Add student to review queue (Queue FIFO)")
    print("13. Process review queue (Queue FIFO)")
    print("14. Exit")


# =======================================================
# MAIN PROGRAM
# =======================================================

def main():
    manager = GradeManager()
    option = 0
    while option != 14:
        show_menu()
        try:
            option = int(input("Select an option: "))
        except ValueError:
            option = 0

        if option == 1:
            manager.register_student()
        elif option == 2:
            manager.display_students_list()
        elif option == 3:
            manager.count_passed_failed()
        elif option == 4:
            manager.update_grade()
        elif option == 5:
            manager.delete_course()
        elif option == 6:
            manager.delete_student()
        elif option == 7:
            sorted_list = manager.bubble_sort()
            print("\nStudents sorted by average (Bubble Sort):")
            manager.display_students_list(sorted_list)
        elif option == 8:
            sorted_list = manager.insertion_sort()
            print("\nStudents sorted alphabetically (Insertion Sort):")
            manager.display_students_list(sorted_list)
        elif option == 9:
            search_name = input("Enter name to search (Linear): ").strip()
            result = manager.linear_search(search_name)
            if result:
                print(f"\nFound: {result.name} - Average: {result.calculate_average():.2f}")
            else:
                print("Student not found.")
        elif option == 10:
            search_name = input("Enter name to search (Binary): ").strip()
            result = manager.binary_search(search_name)
            if result:
                print(f"\nFound: {result.name} - Average: {result.calculate_average():.2f}")
            else:
                print("Student not found.")
        elif option == 11:
            manager.display_history()
        elif option == 12:
            manager.add_to_revision_queue()
        elif option == 13:
            manager.process_revision_queue()
        elif option == 14:
            print("Thank you for using the Academic Grade Manager (Milestone 06).")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
