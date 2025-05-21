from student import Student

def prompt_for_integer(message):
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid whole number.")

def prompt_for_float(message):
    """Prompt the user until a valid floating-point number is entered."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

def run_grade_system():
    all_students = []
    total = prompt_for_integer("Enter total number of students: ")

    for index in range(1, total + 1):
        print(f"\nEntering data for student {index}")
        name = input("Enter student name: ").strip()
        subject_count = prompt_for_integer("Enter number of subjects: ")

        student = Student(name, subject_count)

        for s in range(1, subject_count + 1):
            score = prompt_for_float(f"Enter score for subject {s}: ")
            student.record_score(s - 1, score)

        student.compute_average()
        all_students.append(student)

    print("\n=== GRADE REPORT ===")
    for s in all_students:
        s.display_report()

if __name__ == "__main__":
    run_grade_system()
