def get_valid_number(prompt, min_val=0, max_val=None):
    """Get a valid number from user with validation"""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Cannot exceed {max_val}")
                continue
            return value
        except ValueError:
            print("Pls enter a valid number!")
def get_valid_choice(prompt, min_choice, max_choice):
    """Get a valid menu choice"""
    while True:
        try:
            choice = int(input(prompt))
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Please choose between {min_choice} and {max_choice}")
        except ValueError:
            print("Please enter a valid number!")
def get_non_empty_input(prompt):
    """Get input that cannot be empty"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty!")
def save_session_safely(group_name, member_name, subject, hours, notes):
    """Save session with error handling"""
    try:
        with open("group_study_safe.txt", "a") as file:
            file.write(f"{group_name}|{member_name}|{subject}|{hours}|{notes}\n")
        print("Session saved successfully!\n")
        return True
    except Exception as e:
        print(f"Error saving session: {e}\n")
        return False
def load_sessions_safely():
    """Load all sessions with error handling"""
    sessions = []
    try:
        with open("group_study_safe.txt", "r") as file:
            for line_num, line in enumerate(file, 1):
                try:
                    parts = line.strip().split("|")
                    if len(parts) != 5:
                        print(f"Warning: Skipped corrupted line {line_num}")
                        continue
                    sessions.append({
                        "group": parts[0],
                        "member": parts[1],
                        "subject": parts[2],
                        "hours": float(parts[3]),
                        "notes": parts[4]

                })
                except (ValueError, IndexError) as e:
                    print(f"Warning: Skipped corrupted line {line_num}: {e}")
                    continue
        return sessions
    except FileNotFoundError:
        return []
def add_session():
    """Add new session with full validation"""
    print("\n=== ADD NEW STUDY SESSION ===\n")
    group_name  = get_non_empty_input("Group name: ")
    member_name = get_non_empty_input("Member name: ")
    subject = get_non_empty_input("Subject studied: ")
    hours = get_valid_number("Hours studied (0-24): ", 0, 24)
    notes = input("Quick notes (optional): ").strip()
    if not notes:
        notes = "No notes"
    save_session_safely(group_name, member_name, subject, hours, notes)
def view_group_summary(group_name):
    """View all sessions for a specific group"""
    sessions = load_sessions_safely()
    group_sessions = [s for s in sessions if s["group"] == group_name]
    if not group_sessions:
        print(f"\nNo sessions found for '{group_name}'\n")
        return
    print("\n" + "="* 70)
    print(f"{group_name.upper()} - SESSION HISTORY")
    print("="*70)
    member_hours = {}
    for session in group_sessions:
        member = session["member"]
        print(f"\n {member}")
        print(f" {session['subject']}")
        print(f" {session['hours']} hours")
        print(f" {session['notes']}")
        if member not in member_hours:
            member_hours[member] = 0
        member_hours[member] += session['hours']
    total_hours = sum(member_hours.values())
    num_members = len(member_hours)
    print("\n" + "="*70)
    print("GROUP STATISTICS")
    print("="*70)
    print(f"Total sessions: {len(group_sessions)}")
    print(f"Active members: {num_members}")
    print(f"Total hours: {total_hours:.1f}")
    print(f"Average per member: {total_hours/num_members:.1f} hours")
    top_member = max(member_hours, key=member_hours.get)
    print(f"\n Top contributor: {top_member} ({member_hours[top_member]:.1f} hours)")
    print("="*70 + "\n")
def view_all_groups():
    """Show all unique groups"""
    sessions = load_sessions_safely()
    if not sessions:
        print("\nNo sessions recorded yet!\n")
        return
    groups = set(s["group"] for s in sessions)
    print("\n" + "="*50)
    print("ALL STUDY GROUPS")
    print("="*50)
    for group in sorted(groups):
        count = sum(1 for s in sessions if s["group"] == group)
        total_hours = sum(s["hours"] for s in sessions if s["group"] == group)
        print(f"{group}")
        print(f"Sessions: {count}")
        print(f"Total hours: {total_hours:.1f}\n")
    print("="*50 + "\n")
def main_menu():
    """Main program with error handling"""
    print("BETTER GRUPPE STUDY TRACKER")
    print("Now with bulletproof error handling!\n")
    while True:
        try:
            print("="*50)
            print("MAIN MENU")
            print("="*50)
            print("1. Add study session")
            print("2. View group summary")
            print("3. View all groups")
            print("4. Exit")
            choice = get_valid_choice("\nYour choice(1-4):  ", 1, 4)
            if choice == 1:
                add_session()
            elif choice == 2:
                group_name = get_non_empty_input("\nEnter group name: ")
                view_group_summary(group_name)
            elif choice == 3:
                view_all_groups()
            else:
                print("\nKeep studying together! Goodbye!\n")
                break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting safely...\n")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("Please try again.\n")
if __name__ == "__main__":
    main_menu()
    