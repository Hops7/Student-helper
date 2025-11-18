class GroupMember:
    """Represents a member of a study group"""
    def __init__(self, name, student_id, email):
        """Initialize a group member"""
        self.name = name
        self.student_id = student_id
        self.email = email
        self.total_hours = 0
        self.sessions_attended = 0
        self.subjects_studied = []
    def log_session(self, hours, subject):
        """Log a study session for this member"""
        self.total_hours += hours
        self.sessions_attended += 1 
        if subject not in self.subjects_studied:
            self.subjects_studied.append(subject)
        print(f"Logged {hours}hr session for {self.name}")
    def get_average_hours(self):
        """Calculate average hours per session"""
        if self.sessions_attended == 0:
            return 0
        return self.total_hours / self.sessions_attended
    def display_stats(self):
        """Display member statistics"""
        avg = self.get_average_hours()
        print(f"\n{self.name}'s Statistics:")
        print(f"Student ID: {self.student_id}")
        print(f"Total hours: {self.total_hours:.1f}")
        print(f"Sessions: {self.sessions_attended}")
        print(f"Avg hours/sesion: {avg:.1f}")
        print(f"Subjects: {', '.join(self.subjects_studied)}")
class StudyGroup:
    """Represents a study group with multiple members"""
    def __init__(self, group_name, subject_focus):
        """Initialize a study group"""
        self.group_name = group_name
        self.subject_focus = subject_focus
        self.members = []
        self.total_sessions = 0
    def add_member(self, member):
        """Add a member to the group"""
        self.members.append(member)
        print(f"{member.name} joined {self.group_name}!")
    def remove_member(self, member_name):
        """Remove a member from the group"""
        for member in self.members:
            if member.name == member_name:
                self.members.remove(member)
                print(f"{member_name} left {self.group_name}")
                return
        print(f"{member_name} not found in group")
    def get_member(self, name):
        """Find and return a member by name"""
        for member in self.members:
            if member.name == name:
                return member
        return None
    def log_group_session(self, member_name, hours, subject):
        """Log a session for a specific member"""
        member = self.get_member(member_name)
        if member:
            member.log_session(hours, subject)
            self.total_sessions += 1
        else:
            print(f"{member_name} is not in this group")
    def get_total_hours(self):
        """Calculate total hours for all members"""
        total = 0
        for member in self.members:
            total += member.total_hours
        return total
    def find_top_contributor(self):
        """Find member with most hours"""
        if not self.members:
            return None
        top_member = self.members[0]
        for member in self.members:
            if member.total_hours > top_member.total_hours:
                top_member = member
        return top_member
    def display_group_summary(self):
        """Display comprehensive group statistics"""
        print(f"\n{'='*60}")
        print(f"{self.group_name.upper()}")
        print("Focus: {self.subject_focus}")
        print(f"{'='*60}")
        if not self.members:
            print("No members yet!")
            return
        print(f"\nTotal Members: {len(self.members)}")
        print(f"Total Sessions: {self.total_sessions}")
        print(f"Total Group Hours: {self.get_total_hours():.1f}")
        print(f"\n--- Member List ---")
        for member in self.members:
            print(f"• {member.name} ({member.total_hours:.1f} hours)")
        top = self.find_top_contributor()
        if top:
            print(f"\nTop Contributor: {top.name} ({top.total_hours:.1f} hours)")
        print(f"{'='*60}\n")
def main():
    """Demonstrate the study group system"""
    print("STUDY GROUP MANAGEMENT SYSTEM\n")
    python_group = StudyGroup("Python Warriors", "Programming")
    print(f"Created group: {python_group.group_name}\n")
    member1 = GroupMember("Alex Rodriguez", "S001", "alex@email.com")
    member2 = GroupMember("Jordan Lee", "S002", "jordan@email.com")
    member3 = GroupMember("Sam Taylor", "S003", "sam@email.com")
    python_group.add_member(member1)
    python_group.add_member(member2)
    python_group.add_member(member3)
    print()
    print("--- Logging Study Sessions ---\n")
    python_group.log_group_session("Alex Rodriguez", 3, "Python Basics")
    python_group.log_group_session("Alex Rodriguez", 2, "Data Structures")
    python_group.log_group_session("Jordan Lee", 4, "Python Basics")
    python_group.log_group_session("Jordan Lee", 1.5, "Algorithms")
    python_group.log_group_session("Sam Taylor", 2.5, "Python Basics")
    print("\n--- Individual Statistics ---")
    member1.display_stats()
    member2.display_stats()
    member3.display_stats()
    python_group.display_group_summary()
    print("\n" + "="*60)
    print("Creating second group...\n")
    math_group = StudyGroup("Math Masters", "Mathematics")
    member4 = GroupMember("Casey Johnson", "S004", "casey@email.com")
    member5 = GroupMember("Riley Chen", "S005", "riley@email.com")
    math_group.add_member(member4)
    math_group.add_member(member5)
    math_group.log_group_session("Casey Johnson", 3.5, "Calculus")
    math_group.log_group_session("Riley Chen", 2, "Linear Algebra")
    math_group.display_group_summary()
if __name__ == "__main__":
    main()
