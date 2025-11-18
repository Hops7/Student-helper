class Student:
    """Represents a student in a study group"""
    def __init__(self, name, age, major):
        """Initialize a new student"""
        self.name = name
        self.age = age
        self.major = major
        self.courses = []
        self.gpa = 0.0
    def add_course(self, course_name):
        """Add a course to student's list"""
        self.courses.append(course_name)
        print(f"{self.name} enrolled in {course_name}")
    def set_gpa(self, gpa):
        """Set student's GPA"""
        self.gpa = gpa
    def display_info(self):
        """Display all student information"""
        print(f"\n{'='*40}")
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.age}")
        print(f"GPA: {self.gpa}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"{'='*40}\n")
print("Creating students...\n")
student1 = Student("Alex Rodriguez", 20, "Computer Science")
student2 = Student("Jordan Lee", 19, "Mathematics")
student3 = Student("Sam Taylor", 21, "Physics")
student1.add_course("Python Programming")
student1.add_course("Data Structures")
student1.set_gpa(3.8)
student2.add_course("Calculus")
student2.add_course("Linear Algebra")
student2.set_gpa(3.9)
student3.add_course("Quantum Mechanics")
student3.set_gpa(3.7)
print("\n--- Student Directory ---")
student1.display_info()
student2.display_info()
student3.display_info()
print(f"{student1.name} is studying {student1.major}")
print(f"{student2.name} has a GPA of {student2.gpa}")
class StudySession:
    """Represents a single study session"""
    def __init__(self, subject, duration):
        """Initialize a study session"""
        self.subject = subject
        self.duration = duration
        self.completed = False
    def complete(self):
        """Mark session as completed"""
        self.completed = True
        print(f"Completed {self.duration}hr session on {self.subject}")
        def get_status(self):
            """Return session status"""
            status = "Completed" if self.completed else "In Progress"
            return f"{self.subject}: {self.duration}hrs - {status}"
print("\n--- Study Sessions ---\n")
session1 = StudySession("Python", 3)
session2 = StudySession("Math", 2)
session1.complete()
print(session1.get_status())
print(session2.get_status())
session2.complete()
print(session2.get_status())
