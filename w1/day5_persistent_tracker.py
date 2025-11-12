def save_group_session(group_name, subject, members_present, hours, notes):
    """Save a study session to file"""
    with open("study_session.txt", "a") as file:
        file.write(f"{group_name}|{subject}|{members_present}|{hours}|{notes}\n")
    print("Session saved!\n")

def view_all_sessions():
    """Display all saved study sessions"""
    try:
        with open("study_session.txt", "r") as file:
            sessions = file.readlines()

            if not sessions:
                print("No sessions yet. Start studying!\n")
                return
        
            print("\n" + "="*50)
            print("YOUR STUDY HISTORY")
            print("="*50)

            for session in sessions:
                parts = session.strip().split("|")
                group_name = parts[0]
                subject = parts[1]
                members = parts[2]
                hours = float(parts[3])
                notes = parts[4]

                print(f"{group_name} - {subject}: {hours} hrs ({members} members) - {notes}")
        
            print("="*50 + "\n")
    except FileNotFoundError:
            print("No sessions yet. Start studying!\n")
        
def calculate_group_stats():
    """Calculate and display group statistics"""
    try:
        with open("study_session.txt", "r") as file:
            sessions = file.readlines()

            if not sessions:
                print("No data yet!\n")
                return
            
            total_hours = 0
            total_members = 0
            subjects = {}

            for session in sessions:
                parts = session.strip().split("|")
                hours = float(parts[3])
                members = int(parts[2])
                subject = parts[1]

                total_hours += hours
                total_members += members

                if subject in subjects:
                    subjects[subject] += hours
                else:
                    subjects[subject] = hours
            avg_members = total_members / len(sessions)
            avg_hours_per_session = total_hours / len(sessions)

            print("\n" + "="*70)
            print("GROUP STATISTICS")
            print("="*70)
            print(f"Total sessions: {len(sessions)}")
            print(f"Total study hours: {total_hours}")
            print(f"Average members per session: {avg_members:.1f}")
            print(f"Average hours per session: {avg_hours_per_session:.1f}")

            print("\nHours by subject:")
            for subject, hours in subjects.items():
                print(f" {subject}: {hours} hours")
            
            print("="*70 + "\n")
    except FileNotFoundError:
        print("No data yet!\n")

def main_menu():
    """Main program loop"""
    print("GROUP STUDY TRACKER")
    print("Track your study group's progress together!\n")

    while True:
        print("=" *70)
        print("MENU")
        print("="*70)
        print("1. Add new group study session")
        print("2. View all sessions")
        print("3. View group statistics")
        print("4. Exit")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            print("\n--- NEW GROUP SESSION ---")
            group_name = input("Group name: ")
            subject = input("Subject studied: ")
            members_present = int(input("Number of members present: "))
            total_hours = float(input("Total combined hours: "))
            notes = input("Quick notes about the session: ")

            save_group_session(group_name, subject, members_present, total_hours, notes)

        elif choice == "2":
            view_all_sessions()
        elif choice == "3":
            calculate_group_stats()
        elif choice == "4":
            print("\nKeep studying together! See ya!\n")
            break
        else:
            print("\nInvalid choice. Please pick 1-4.\n")
if __name__ == "__main__":
    main_menu()
