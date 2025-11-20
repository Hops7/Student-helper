from datetime import datetime
class GroupMember:
    """Represents a member with advanced features"""
    all_members = []
    def __init__(self, name, student_id, email):
        """Initialize member"""
        self.name = name
        self.student_id = student_id
        self.email = email
        self._hours_studied = 0
        self._sessions = []
        self.joined_date = datetime.now().strftime("%Y-%m-%d")
        GroupMember.all_members.append(self)
    def log_session(self, hours, subject, difficulty):
        """Log a study session with details"""
        session = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "hours": hours,
            "subject": subject,
            "difficulty": difficulty
        }
        self._sessions.append(session)
        self._hours_studied += hours
    @property
    def total_hours(self):
        """Get total hours studied"""
        return self._hours_studied
    @property
    def session_count(self):
        """Get number of sessions"""
        return len(self._sessions)
    @property
    def average_hours(self):
        """Calculate average hours per session"""
        if len(self._sessions) == 0:
            return 0
        return self._hours_studied / len(self._sessions)
    @property
    def rank(self):
        """Determine member rank based on hours"""
        if self._hours_studied >= 50:
            return "Master Scholar"
        elif self._hours_studied >= 30:
            return "Advanced Learner"
        elif self._hours_studied >= 15:
            return "Active Student"
        elif self._hours_studied >= 5:
            return "Emerging Scholar"
        else:
            return "New Member"
    @property
    def recent_activity(self):
        """Get last 3 sessions"""
        return self._sessions[-3:]
    def __str__(self):
        """String representation"""
        return f"{self.name} - {self.rank} ({self._hours_studied:.1f}hrs)"
    def __repr__(self):
        """Developer representation"""
        return f"GroupMember('{self.name}', '{self.student_id}')"
    def display_full_stats(self):
        """Display comprehensive statistics"""
        print(f"\n{'='*50}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print(f"Joined: {self.joined_date}")
        print(f"Rank: {self.rank}")
        print(f"Total Hours: {self._hours_studied:.1f}")
        print(f"Sessions: {self.session_count}")
        print(f"Avg Hours/Session: {self.average_hours:.1f}")
        if self._sessions:
            print(f"\nRecent Activity:")
            for session in self.recent_activity:
                print(f" • {session['date']}: {session['subject']}"
                    f" ({session['hours']}hrs, {session['difficulty']})")
        print(f"{'='*50}\n")
    @classmethod
    def get_total_members(cls):
        """Get total number of members"""
        return len(cls.all_members)
    @classmethod
    def find_member_by_id(cls, student_id):
        """Find a member by student ID"""
        for member in cls.all_members:
            if member.student_id == student_id:
                return member
        return None
class StudyGroup:
    """Represents a study group with advanced features"""
    all_groups = []
    total_groups_created = 0
    def __init__(self, name, subject, max_members=20):
        """Initialize study group"""
        self.name = name
        self.subject = subject
        self.max_members = max_members
        self.members = []
        self.created_date = datetime.now().strftime("%Y-%m-%d")
        self._is_active = True
        StudyGroup.all_groups.append(self)
        StudyGroup.total_groups_created += 1
    def add_member(self, member):
        """Add member with validation"""
        if len(self.members) >= self.max_members:
            print(f"{self.name} is full! (max {self.max_members} members)")
            return False
        if member in self.members:
            print(f"{member.name} is already in {self.name}")
            return False
        self.members.append(member)
        print(f"{member.name} joined {self.name}!")
        return True
    def remove_member(self, member):
        """Remove a member"""
        if member in self.members:
            self.members.remove(member)
            print(f"{member.name} left {self.name}")
            return True
        print(f"{member.name} not in {self.name}")
        return False
    @property
    def member_count(self):
        """Get current number of members"""
        return len(self.members)
    @property
    def total_group_hours(self):
        """Calculate total hours for entire group"""
        return sum(member.total_hours for member in self.members)
    @property
    def average_member_hours(self):
        """Calculate average hours per member"""
        if not self.members:
            return 0 
        return self.total_group_hours / len(self.members)
    @property
    def is_full(self):
        """Check if group is at capacity"""
        return len(self.members) >= self.max_members
    @property
    def group_status(self):
        """Determine group status"""
        if not self._is_active:
            return "Inactive"
        elif self.total_group_hours >= 100:
            return "Highly Active"
        elif self.total_group_hours >= 50:
            return "Active"
        elif self.total_group_hours >= 10:
            return "Growing"
        else:
            return "New"
    @property
    def top_contributor(self):
        """Find member with most hours"""
        if not self.members:
            return None
        return max(self.members, key=lambda m: m.total_hours)
    def __str__(self):
        """String representation"""
        return f"{self.name} ({self.subject}) - {self.member_count}/{self.max_members} members - {self.group_status}"
    def __repr__(self):
        """Developer representation"""
        return f"StudyGroup('{self.name}', '{self.subject}')"
    def display_summary(self):
        """Display comprehensive group summary"""
        print(f"\n{'='*70}")
        print(f"{self.name.upper()} - COMPREHENSIVE SUMMARY")
        print(f"{'='*70}")
        print(f"Subject Focus: {self.subject}")
        print(f"Created: {self.created_date}")
        print(f"Status: {self.group_status}")
        print(f"Members: {self.member_count}/{self.max_members}")
        print(f"Total Group Hours: {self.total_group_hours:.1f}")
        print(f"Average Hours/Member: {self.average_member_hours:.1f}")
        if self.members:
            print(f"\n--- Member Roster ---")
            sorted_members = sorted(self.members, key=lambda m: m.total_hours, reverse=True)
            for i, member in enumerate(sorted_members, 1):
                emoji = "🏅🏅🏅" if i == 1 else "🏅🏅" if i == 2 else "🏅" if i == 3 else f"{i}."
                print(f"{emoji} {member.name}: {member.total_hours:.1f}hrs ({member.session_count} sessions)")
            if self.top_contributor:
                print(f"\n🎊 Top Contributor: {self.top_contributor.name} ({self.top_contributor.total_hours:.1f} hours)")
        print(f"{'='*70}\n")
    def deactivate(self):
        """Deactivate the group"""
        self._is_active = False
        print(f"{self.name} has been deactivated")
    def activate(self):
        """Reactivate the group"""
        self._is_active = True
        print(f"{self.name} has been reactivated")
    @classmethod
    def get_all_active_groups(cls):
        """Get list of all active groups"""
        return [group for group in cls.all_groups if group._is_active]
    @classmethod
    def find_group_by_name(cls, name):
        """Find a group by name"""
        for group in cls.all_groups:
            if group.name.lower() == name.lower():
                 return group
        return None
    @classmethod
    def get_statistics(cls):
        """Get overall statistics for all groups"""
        total_members = sum(group.member_count for group in cls.all_groups)
        total_hours = sum(group.total_group_hours for group in cls.all_groups)
        active_groups = len(cls.get_all_active_groups())
        return {
            "total_groups": cls.total_groups_created,
            "active_groups": active_groups,
            "total_members": total_members,
            "total_hours": total_hours
        }
def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("ENHANCED STUDY GROUP MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Create new group")
    print("2. Create new member")
    print("3. Add member to group")
    print("4. Log study session")
    print("5. View member statistics")
    print("6. View group summary")
    print("7. View all groups")
    print("8. View system statistics")
    print("9. Exit")
    print("="*60)
def get_choice(prompt, min_val, max_val):
    """Get validated menu choice"""
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            print(f"Please choose between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number!")
def get_input(prompt):
    """Get non-empty input"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty!")
def create_group():
    """Create a new study"""
    print("\n--- CREATE NEW GROUP ---")
    name = get_input("Group name: ")
    subject = get_input("Subject focus: ")

    try:
        max_members = int(input("Max members default 20): ") or "20")
        group = StudyGroup(name, subject, max_members)
        print(f"Group '{name}' created successfully!")
        return group
    except ValueError:
        print("Invalid number. Using default max of 20.")
        group = StudyGroup(name, subject)
        return group
def create_member():
    """Create a new member"""
    print("\n--- CREATE NEW MEMBER ---")
    name = get_input("Full name: ")
    student_id = get_input("Student ID: ")
    email = get_input("Email: ")
    member = GroupMember(name, student_id, email)
    print(f"Member '{name}' created successfully!")
    return member
def add_member_to_group():
    """Add an existing member to a group"""
    print("\n--- ADD MEMBER TO GROUP ---")
    if not StudyGroup.all_groups:
        print("No groups exist yet!")
        return
    print("\nAvailable Groups: ")
    for i, group in enumerate(StudyGroup.all_groups, 1):
        print(f"{i}. {group}")
    group_choice = get_choice(f"\nSelect group (1-{len(StudyGroup.all_groups)}): ",
                              1, len(StudyGroup.all_groups))
    selected_group = StudyGroup.all_groups[group_choice - 1]
    if not GroupMember.all_members:
        print("No members exist yet!")
        return
    print("\nAvailable Members:")
    for i, member in enumerate(GroupMember.all_members, 1):
        print(f"{i}. {member.name} ({member.student_id})")
    member_choice = get_choice(f"\nSelect member (1-{len(GroupMember.all_members)}): ",
                               1, len(GroupMember.all_members))
    selected_member = GroupMember.all_members[member_choice - 1]
    selected_group.add_member(selected_member)
def log_session():
    """Log a study session for a member"""
    print("\n--- LOG STUDY SESSION ---")
    if not GroupMember.all_members:
        print("No members exist yet!")
        return
    print("\nMembers:")
    for i, member in enumerate(GroupMember.all_members, 1):
        print(f"{i}. {member.name}")
    member_choice = get_choice(f"\nSelect member (1-{len(GroupMember.all_members)}): ",
                               1, len(GroupMember.all_members))
    member = GroupMember.all_members[member_choice - 1]
    while True:
        try:
            hours = float(input("Hours studied: "))
            if hours > 0:
                break
            print("Hours must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    subject = get_input("Subject: ")
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    diff_choice = get_choice("Select difficulty (1-3): ", 1, 3)
    difficulty = ["easy", "medium", "hard"][diff_choice - 1]
    member.log_session(hours, subject, difficulty)
    print(f"\nSession logged for {member.name}!")
    print(f"Total hours: {member.total_hours:.1f}")
    print(f"Current rank: {member.rank}")
def view_member_stats():
    """View detailed member statistics"""
    print("\n--- MEMBER STATISTICS ---")
    if not GroupMember.all_members:
        print("No members exist yet!")
        return
    print("\nMembers:")
    for i, member in enumerate(GroupMember.all_members, 1):
        print(f"{i}. {member.name}")
    member_choice = get_choice(f"\nSelect member (1-{len(GroupMember.all_members)}): ",
                               1, len(GroupMember.all_members))
    member = GroupMember.all_members[member_choice - 1]
    member.display_full_stats()
def view_group_summary():
    
    """View group summary"""
    print("\n--- GROUP SUMMARY ---")
    if not StudyGroup.all_groups:
        print("No groups exist yet!")
        return
    print("\nGroups: ")
    for i, group in enumerate(StudyGroup.all_groups, 1):
        print(f"{i}. {group.name}")
    group_choice = get_choice(f"\nSelect group(1-{len(StudyGroup.all_groups)}): ",
                              1, len(StudyGroup.all_groups))
    group = StudyGroup.all_groups[group_choice - 1]
    group.display_summary()
def view_all_groups():
    """View list of all groups"""
    print("\n--- ALL GROUPS ---")
    if not StudyGroup.all_groups:
        print("No groups exist yet!")
        return
    print(f"\n{'='*70}")
    for group in StudyGroup.all_groups:
        print(group)
    print(f"{'='*70}\n")
def view_system_stats():
    """View overall system statistics"""
    print("\n" + "="*60)
    print("SYSTEM-WIDE STATISTICS")
    print("="*60)
    stats = StudyGroup.get_statistics()
    print(f"Total Groups Created: {stats['total_groups']}")
    print(f"Active Groups: {stats['active_groups']}")
    print(f"Total Members: {GroupMember.get_total_members()}")
    print(f"Total Study Hours: {stats['total_hours']:.1f}")
    if stats['total_hours'] > 0:
        print(f"Average Hours/Member: {stats['total_hours']/GroupMember.get_total_members():.1f}")
    if GroupMember.all_members:
        top_member = max(GroupMember.all_members, key=lambda m: m.total_hours)
        print(f"🎊 Top Member Overall: {top_member.name} ({top_member.total_hours:.1f} hours)")
    if StudyGroup.all_groups:
        top_group = max(StudyGroup.all_groups, key=lambda g: g.total_group_hours)
        print(f"🎊 Most Active Group: {top_group.name} ({top_group.total_group_hours:.1f} hours)")
    print("="*60 + "\n")
def main():
    """Main program loop"""
    print("\n" + "="*60)
    print("ENHANCED STUDY GROUP MANAGEMENT SYSTEM")
    print("Day 9 Project - Advanced OOP Features")
    print("="*60)
    print("\n--- Creating Sample Data ---\n")
    group1 = StudyGroup("Python Warriors", "Programming", 15)
    group2 = StudyGroup("Math Masters", "Mathematics", 20)
    member1 = GroupMember("Alex Rodriguez", "S001", "alex@email.com")
    member2 = GroupMember("Jordan Lee", "S002", "jordan@email.com")
    member3 = GroupMember("Sam Taylor", "S003", "sam@email.com")
    group1.add_member(member1)
    group1.add_member(member2)
    group2.add_member(member3)
    member1.log_session(3, "Python Basics", "medium")
    member1.log_session(2.5, "OOP Concepts", "hard")
    member2.log_session(4, "Data Structures", "medium")
    member3.log_session(2, "Calculus", "hard")
    print("\nSample data created! Ready to use the system.\n")
    while True:
        try:
            display_menu()
            choice = get_choice("\nYour choice (1-9): ", 1, 9)
            if choice == 1:
                create_group()
            elif choice == 2:
                create_member()
            elif choice == 3:
                add_member_to_group()
            elif choice == 4:
                log_session()
            elif choice == 5:
                view_member_stats()
            elif choice == 6:
                view_group_summary()
            elif choice == 7:
                view_all_groups()
            elif choice == 8:
                view_system_stats()
            else:
                print("\n" + "="*60)
                print("Thank you for using the system!")
                print("Keep studying and growing!")
                print("="*60 + "\n")
                break
        except KeyboardInterrupt:
            print("\n\nExiting safely...\n")
            break
        except Exception as e:
            print(f"\nAn error occured: {e}")
            print("Please try again.\n")
if __name__ == "__main__":
    main()