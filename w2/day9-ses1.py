class StudyGroup:
    """Enhanced study group with class variables"""
    total_groups = 0
    all_group_names = []
    def __init__(self, name, subject):
        """Initialize study group"""
        self.name = name
        self.subject = subject
        self.members = []
        self._total_hours = 0
        StudyGroup.total_groups += 1
        StudyGroup.all_group_names.append(name)
    def add_hours(self, hours):
        """Add study hours with validation"""
        if hours > 0:
             self._total_hours += hours
        else:
            print("Hours must be positive!")
    @property
    def total_hours(self):
        """Getter for total hours"""
        return self._total_hours
    @property
    def total_hours(self):
        """Getter for total hours"""
        return self._total_hours
    @property
    def group_size(self):
        """Computed property - number of members"""
        return len(self.members)
    @property
    def performance_rating(self):
        """Computed property based on hours"""
        if self._total_hours >= 50:
            return "Excellent!!!"
        elif self._total_hours >= 20:
            return "Good!!"
        elif self._total_hours >= 5:
            return "Fair!"
        else:
            return "New Group"
    def __str__(self):
        """User-firendly string representation"""
        return f"{self.name} - {self.subject} ({self.group_size} members)"
    def __repr__(self):
        """Developer representation"""
        return f"StudyGroup('{self.name}', '{self.subject}')"
    @classmethod
    def get_total_groups(cls):
        """Class method to get total groups"""
        return cls.total_groups
    @classmethod
    def list_all_groups(cls):
        """Class method to list all groups"""
        return cls.all_group_names
class GroupMember:
    """Enhanced group member with properties"""
    def __init__(self, name, student_id):
        """Initialize member"""
        self.name = name
        self.student_id = student_id
        self._hours_studied = 0
        self._sessions = 0
    def log_session(self, hours):
        """Log a study session"""
        self._hours_studied += hours
        self._sessions += 1
    @property
    def hours_studied(self):
        """Getter for hours"""
        return self._hours_studied
    @property
    def average_session_lenght(self):
        """Computed property"""
        if self._sessions == 0:
            return 0
        return self._hours_studied / self._sessions
    @property
    def dedication_level(self):
        """Computed property for dedication"""
        if self._hours_studied >= 30:
            return "Highly Dedicated!"
        elif self._hours_studied >= 15:
            return "Dedicated!"
        elif self._hours_studied >= 5:
            return "Getting Momentum"
        else:
            return "Getting started"
    def __str__(self):
        """String representation"""
        return f"{self.name} ({self.student_id}): {self._hours_studied}hrs"
print("="*60 + "\n")
print("ADVANCED OOP DEMONSTRATION")
("="*60 + "\n")
group1 = StudyGroup("Python Warriors", "Programming")
group2 = StudyGroup("Math Masters", "Mathematics")
group3 = StudyGroup("Physics Phenom", "Physics")
print("--- Created Groups ---")
print(group1)
print(group2)
print(group3)
print()
group1.add_hours(25)
group2.add_hours(55)
group3.add_hours(8)
print("--- Group Performance ---")
print(f"{group1.name}: {group1.total_hours}hrs - {group1.performance_rating}")
print(f"{group2.name}: {group2.total_hours}hrs - {group2.performance_rating}")
print(f"{group3.name}: {group3.total_hours}hrs - {group3.performance_rating}")
print()
print("--- Class-Level Statistics ---")
print(f"Total groups created: {StudyGroup.get_total_groups()}")
print(f"All groups {', '.join(StudyGroup.list_all_groups())}")
print()
member1 = GroupMember("Alex", "S001")
member2 = GroupMember("Jordan", "S002")
member1.log_session(3)
member1.log_session(2.5)
member1.log_session(4)
member2.log_session(20)
member2.log_session(15)
print("--- Member Statistics ---")
print(member1)
print(f" Average Session: {member1.average_session_lenght:.1f}hrs")
print(f" Status: {member1.dedication_level}")
print()
print(member2)
print(f" Average session: {member2.average_session_lenght:.1f}hrs")
print(f" Status: {member2.dedication_level}")