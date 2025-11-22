from datetime import datetime, date, timedelta
class StudySession:
    """Represents a single study session with date/time"""
    def __init__(self, subject, duration, difficulty, notes=""):
        """Initialize a study session"""
        self.subject = subject
        self.duration = duration
        self.difficulty = difficulty
        self.notes = notes
        self.timestamp = datetime.now()
        self.completed = False
    def complete(self):
        """Mark session as completed"""
        self.completed = True
    @property
    def date(self):
        """Get just the date"""
        return self.timestamp.date()
    @property
    def time(self):
        """Get formatted time"""
        return self.timestamp.strftime("%I:%M %p")
    @property
    def formatted_date(self):
        """Get nicely formatted date"""
        return self.timestamp.strftime("%B %d, %Y")
    @property
    def days_ago(self):
        """Calculate days since session"""
        delta = date.today() - self.date
        return delta.days
    def __str__(self):
        """String representation"""
        status = "✅" if self.completed else "⏳"
        return f"{status} {self.subject} - {self.duration}hrs ({self.formatted_date})"
    def get_details(self):
        """Get detailed session information"""
        return {
            "subject": self.subject,
            "duration": self.duration,
            "difficulty": self.difficulty,
            "notes": self.notes,
            "date": self.formatted_date,
            "time": self.time,
            "days_ago": self.days_ago,
            "completed": self.completed
        }
class GroupMember:
    """Enhanced member with date tracking"""
    def __init__(self, name, student_id, email):
        """Initialize member"""
        self.name = name
        self.student_id = student_id
        self.email = email
        self.sessions = []
        self.joined_date = date.today()
    def add_session(self, session):
        """Add a study session"""
        self.sessions.append(session)
        session.complete()
        print(f"✅ Session added for {self.name}")
    def create_and_add_session(self, subject, duration, difficulty, notes=""):
        """Create and add a new session"""
        session = StudySession(subject, duration, difficulty, notes)
        self.add_session(session)
        return session
    @property
    def total_hours(self):
        """Calculate total hours studied"""
        return sum(s.duration for s in self.sessions)
    @property
    def session_count(self):
        """Get number of sessions"""
        return len(self.sessions)
    @property
    def days_as_member(self):
        """Calculate days since joining"""
        delta = date.today() - self.joined_date
        return delta.days
    @property
    def last_study_date(self):
        """Get date of last study session"""
        if not self.sessions:
            return None
        return max(s.timestamp for s in self.sessions).date()
    @property
    def study_streak(self):
        """Calculate current study streak in days"""
        if not self.sessions:
            return 0
        sorted_sessions = sorted(self.sessions, key=lambda s: s.date, reverse=True)
        streak = 0
        expected_date = date.today()
        for session in sorted_sessions:
            if session.date == expected_date:
                streak += 1
                expected_date -= timedelta(days=1)
            elif session.date < expected_date:
                break
        return streak
    def get_sessions_this_week(self):
        """Get sessions from the past 7 days"""
        week_ago = date.today() - timedelta(days=7)
        return [s for s in self.sessions if s.date >= week_ago]
    def get_sessions_this_month(self):
        """Get sessions from this month"""
        this_month = date.today().replace(day=1)
        return [s for s in self.sessions if s.date >= this_month]
    def get_sessions_by_subject(self, subject):
        """Get all sessions for a specific subject"""
        return [s for s in self.sessions if s.subject.lower() == subject.lower()]
    def display_recent_activity(self, days=7):
        """Display recent study activity"""
        print(f"\n{'='*60}")
        print(f"{self.name}'s Activity (Last {days} Days)")
        print(f"{'='*60}")
        cutoff_date = date.today() - timedelta(days=days)
        recent = [s for s in self.sessions if s.date >= cutoff_date]
        if not recent:
            print(f"No activity in the last {days} days")
            print(f"{'='*60}\n")
            return
        by_date = {}

        for session in recent:
            date_str = session.formatted_date
            if date_str not in by_date:
                by_date[date_str] = []
            by_date[date_str].append(session)
        for date_str in sorted(by_date.keys(), reverse=True):
            sessions_on_date = by_date[date_str]
            total_hours = sum(s.duration for s in sessions_on_date)
            print(f"\n{date_str} ({total_hours:.1f}hrs total): ")
            for session in sessions_on_date:
                print(f"  • {session.subject}: {session.duration}hrs ({session.difficulty})")
                if session.notes:
                    print(f"   Notes: {session.notes}")
        print(f"\n{'='*60}")
    def __str__(self):
        """String representation"""
        return f"{self.name} - {self.total_hours:.1f}hrs in {self.session_count} sessions"
class StudyGroup:
    """Enhanced group with date tracking"""
    def __init__(self, name, subject):
        """Initialize study group"""
        self.name = name
        self.subject = subject
        self.members = []
        self.created_date = date.today()
    def add_member(self, member):
        """Add a member"""
        if member not in self.members:
            self.members.append(member)
            print(f"✅ {member.name} joined {self.name}")
            return True
        return False
    @property
    def days_active(self):
        """Calculate days since group creation"""
        delta = date.today() - self.created_date
        return delta.days
    @property
    def total_group_hours(self):
        """Calculate total hours for all members"""
        return sum(m.total_hours for m in self.members)
    def get_activity_this_week(self):
        """Get group activity for this week"""
        week_sessions = []
        for member in self.members:
            week_sessions.extend(member.get_sessions_this_week())
        return week_sessions
    def get_most_active_member(self):
        """Find member with most hours"""
        if not self.members:
            return None
        return max(self.members, key=lambda m: m.total_hours)
    def get_most_recent_activity(self):
        """Get most recent session across all members"""
        all_sessions = []
        for member in self.members:
            all_sessions.extend(member.sessions)
        if not all_sessions:
            return None
        return max(all_sessions, key=lambda s: s.timestamp)
    def display_weekly_summary(self):
        """Display summary of this week's activity"""
        print(f"\n{'='*70}")
        week_sessions = self.get_activity_this_week()
        if not week_sessions:
            print("No activity this week")
            print(f"{'='*70}\n")
            print(f"{self.name.upper()} - THIS WEEK'S SUMMARY")
            print(f"{'='*70}")
            return
        total_hours = sum(s.duration for s in week_sessions)
        active_members = len(set(s.subject for s in week_sessions))
        print(f"Week: {(date.today() - timedelta(days=7)).strftime('%b %d')} - {date.today().strftime('%b %d')}")
        print(f"Total Sessions: {len(week_sessions)}")
        print(f"Total Hours: {total_hours:.1f}")
        print(f"Active Members: {len([m for m in self.members if m.get_sessions_this_week()])}")
        print(f"\n--- Member Activity ---")
        for member in self.members:
            member_sessions = member.get_sessions_this_week()
            if member_sessions:
                member_hours = sum(s.duration for s in member_sessions)
                print(f"{member.name}: {len(member_sessions)} sessions, {member_hours:.1f}hrs")
        subjects = {}
        for session in week_sessions:
            subjects[session.subject] = subjects.get(session.subject, 0) + session.duration
        print(f"\n--- Most Studied Subjects ---")
        for subject, hours in sorted(subjects.items(), key=lambda x: x[1], reverse=True):
            print(f"{subject}: {hours:.1f}hrs")
        print(f"\n{'='*70}\n")
def main():
    """Demonstrate date-enhanced system"""
    print("\n" + "="*70)
    print("STUDY GROUP SYSTEM WITH DATE/TIME TRACKING")
    print("Day 10 Project")
    print("="*70 + "\n")
    group = StudyGroup("Python Warriors", "Programming")
    print(f"Created group: {group.name}")
    print(f"Group created: {group.created_date.strftime('%B %d, %Y')}\n")
    alex = GroupMember("Alex Rodriguez", "S001", "alex@email.com")
    jordan = GroupMember("Jordan Lee", "S002", "jordan@email.com")
    sam = GroupMember("Sam Taylor", "S003", "sam@email.com")
    group.add_member(alex)
    group.add_member(jordan)
    group.add_member(sam)
    print()
    print("--- Adding Study Session ---\n")
    session1 = alex.create_and_add_session("Python Basics", 3, "medium", "Learned about variables and loops")
    session2 = alex.create_and_add_session("Data Structures", 2.5, "hard", "Lists and dictionaries")
    session3 = alex.create_and_add_session("OOP Concepts", 4, "hard", "Classes and objects")
    jordan.create_and_add_session("Python Basics", 2, "easy", "Got the fundamentals down")
    jordan.create_and_add_session("Functions", 3.5, "medium", "Writing reusable code")
    sam.create_and_add_session("Python Basics", 2.5, "medium", "Good progress")
    sam.create_and_add_session("File Handling", 1.5, "medium", "Reading and writing files")
    print()
    print("--- Member Statistics ---\n")
    for member in group.members:
        print(f"{member.name}")
        print(f"Joined: {member.joined_date.strftime('%B %d, %Y')} ({member.days_as_member} days ago)")
        print(f"Total Hours: {member.total_hours:.1f}")
        print(f"Sessions: {member.session_count}")
        print(f"Study streak: {member.study_streak} days")
        if member.last_study_date:
            days_since = (date.today() - member.last_study_date).days
            if days_since == 0:
                print(f"Last session: Today")
            elif days_since == 1:
                print(f"Last session: Yesterday")
            else:
                print(f"Last session: {days_since} days ago")
        print()
    alex.display_recent_activity(7)
    group.display_weekly_summary()
    recent = group.get_most_recent_activity()
    if recent:
        print("--- Most Recent Group Activity ---")
        print(f"Subject: {recent.subject}")
        print(f"Duration: {recent.duration} hours")
        print(f"When: {recent.formatted_date} at {recent.time}")
        print(f"Days ago: {recent.days_ago}")
        print()
    print(f"Group has been active for {group.days_active} days")
    print(f"Total group hours: {group.total_group_hours:.1f}")
    print("--- Subject Analysis ---\n")
    python_sessions = alex.get_sessions_by_subject("Python Basics")
    print(f"Alex's 'Python Basics' sessions: {len(python_sessions)}")
    for session in python_sessions:
        print(f"  • {session.formatted_date}: {session.duration}hrs")
    print()
    print(f"Average hours per day: {group.total_group_hours / max(group.days_active, 1):.1f}")
    print("\n" + "="*70 + "\n")
if __name__ == "__main__":
    main()