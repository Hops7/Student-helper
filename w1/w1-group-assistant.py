import random
from datetime import datetime
MOTIVATIONAL_QUOTES = [
    "Together we learn, together we grow!",
    "Your group's effort today builds tomorrow's success.",
    "Small progress is still progress!",
    "Consistency beats perfection - keep showing up!",
    "Every expert was once a beginner.",
    "Study groups succeed because you lift each other up!",
    "The best time to start was yesterday. The next best time is now!",
    "Your dedication inspires your teammates!"
]
def save_session(group_name, member_name, subject, hours, difficulty, mood, notes):
    """Save a study session to file"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("group_assistant_data.txt", "a") as file:
            file.write(f"{timestamp}|{group_name}|{member_name}|{subject}|{difficulty}|{mood}|{notes}\n")
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False
def load_all_sessions():
    """Load all sessions from file"""
    sessions = []
    try:
        with open("group_assistant_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 7:
                    sessions.append({
                        "timestamp": parts[0],
                        "group": parts[1],
                        "member": parts[2],
                        "subject": parts[3],
                        "hours": float(parts[4]),
                        "difficulty": parts[5],
                        "mood": int(parts[6]),
                        "notes": parts[7]
                    })
    except FileNotFoundError:
        pass
    return sessions
def get_valid_number(prompt, min_val, max_val):
    """Get validated number input"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number!")
def get_non_empty(prompt):
    """Get non-empty string input"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty!")
def get_choice(prompt, options):
    """Get validated choice from options"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Please choose from: {', '.join(options)}")
def add_study_session():
    """Add a new study session"""
    print("\n" + "="*60)
    print("ADD NEW STUDY SESSION")
    print("="*60 + "\n")
    group_name = get_non_empty("Group name: ")
    member_name = get_non_empty("Member name: ")
    subject = get_non_empty("Subject studied: ")
    hours = get_valid_number("Hours studied (0-24): ", 0, 24)
    difficulty = get_choice("Difficulty (easy/medium/hard): ", ["easy", "medium", "hard"])
    mood = int(get_valid_number("How motivated did you feel? (1-10): ", 1, 10))
    notes = input("Quick notes (optional): ").strip() or "No notes"
    if save_session(group_name, member_name, subject, hours, difficulty, mood, notes):
        print("\nSession saved successfully!")
        if hours >= 3:
            print("Wow! That's dedication!")
        elif hours >= 2:
            print("Great work!")
        else:
            print("Every bit counts!")
        print()
def view_group_stats(group_name):
    """Show detailed statistics for a group"""
    sessions = [s for s in load_all_sessions() if s["group"] == group_name]
    if not sessions:
        print(f"No sessions found for '{group_name}'\n")
        return
    print("\n" + "="*70)
    print(f"{group_name.upper()} - DETAILED STATISTICS")
    print("="*70 + "\n")
    member_data = {}
    for session in sessions:
        member = session["member"]
        if member not in member_data:
            member_data[member] = {
                "sessions": 0,
                "hours": 0,
                "moods": [],
                "subjects": set()
            }
        member_data[member]["sessions"] += 1
        member_data[member]["hours"] += session["hours"]
        member_data[member]["moods"].append(session["mood"])
        member_data[member]["subjects"].add(session["subject"])
    print("MEMBER BREAKDOWN:")
    print("-" * 70)
    for member, data in sorted(member_data.items(), key=lambda x: x[1]["hours"], reverse=True):
        avg_mood = sum(data["moods"]) / len(data["moods"])
        print(f"\n{member}")
        print(f"Sessions: {data['sessions']}")
        print(f"Total hours: {data['hours']:.1f}")
        print(f"Avg hours/session: {data['hours']/data['sessions']:.1f}")
        print(f"Avg motivation: {avg_mood:.1f}/10")
        print(f"Subjects: {', '.join(data['subjects'])}")
    total_hours = sum(s["hours"] for s in sessions)
    avg_mood = sum(s["mood"] for s in sessions) / len(sessions)
    print("\n" + "="*70)
    print("GROUP TOTALS:")
    print(f"Total sessions: {len(sessions)}")
    print(f"Total hours: {total_hours:.1f}")
    print(f"Active members: {len(member_data)}")
    print(f"Avg motivation: {avg_mood:.1f}/10")
    top_member = max(member_data.items(), key=lambda x: x[1]["hours"])
    print(f"\nTop contributor: {top_member[0]} ({top_member[1]['hours']:.1f} hours)")
    print("="*70 + "\n")
def show_leaderboard():
    """Show leaderboard across all groups"""
    sessions = load_all_sessions()
    if not sessions:
        print("\nNo data yet!\n")
        return
    member_hours = {}
    for session in sessions:
        key = f"{session['member']} ({session['group']})"
        if key not in member_hours:
            member_hours[key] = 0
        member_hours[key] += session['hours']
    print("\n" + "="*60)
    print("GLOBAL LEADERBOARD - TOP STUDENTS")
    print("="*60 + "\n")
    sorted_members = sorted(member_hours.items(), key=lambda x: x[1], reverse=True)
    for rank, (member, hours) in enumerate(sorted_members[:10], 1):
        emoji = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
        print(f"{emoji} #{rank}. {member}: {hours:.1f} hours")
    print("\n" + "="*60 + "\n")
def get_personalized_motivation(group_name):
    """Generate personalized motivation based on progress"""
    sessions = [s for s in load_all_sessions() if s["group"] == group_name]
    if not sessions:
        return "Start your journey today! Your first session is the hardest but most important."
    total_hours = sum(s["hours"] for s in sessions)
    recent_mood = sum(s["mood"] for s in sessions[-5:]) / min(len(sessions), 5)
    message = random.choice(MOTIVATIONAL_QUOTES)
    message += f"\n\nYour group has studied {total_hours:.1f} hours together!"
    if recent_mood >= 8:
        message += "\nYour team's motivation is sky-high - keep that energy!"
    elif recent_mood >= 6:
        message += "\nYour team is staying positive - great mindset!"
    else:
        message += "\nRemember tough days build stronger minds. You've got this!"
    return message
def show_motivation():
    """Display motivational message"""
    group_name = get_non_empty("\nEnter your group name: ")
    print("\n" + "="*60)
    print(f"MOTIVATION FOR {group_name.upper()}")
    print("="*60 + "\n")
    message = get_personalized_motivation(group_name)
    print(message)
    print("\n" + "="*60 + "\n")
def run_group_quiz():
    """Run a quick quiz for the group"""
    print("\n" + "="*60)
    print("GROUP KNOWLEDGE QUIZ")
    print("="*60 + "\n")
    group_name = get_non_empty("Group name: ")
    num_members = int(get_valid_number("How many members taking quiz? ", 1, 10))
    questions = [
        ("What is 15 x 12?", "180"),
        ("What is the capital of Italy?", "Rome"),
        ("How many sides does a hexagon have?", "6"),
        ("What year did the World War II end?", "1945"),
        ("What is the largest planet in our solar system?", "Jupiter")
    ]
    member_scores = []
    for i in range(num_members):
        print(f"\n--- MEMBER {i+1} ---")
        name = get_non_empty("Name: ")
        score = 0
        for q, answer in random.sample(questions, 3):
            print(f"\n{q}")
            user_answer = input("Answer: ").strip().lower()
            if user_answer == answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Answer: {answer}")
        percentage = (score / 3) * 100
        member_scores.append({"name": name, "score": score, "percentage": percentage})
        print(f"\n{name}: {score}/3 ({percentage:.0f}%)")
    print("\n" + "="*60)
    print(f"{group_name.upper()} - QUIZ RESULTS")
    print("="*60 + "\n")
    for member in member_scores:
        print(f"{member['name']}: {member['score']}/3 ({member['percentage']:.0f}%)")
    avg_score = sum(m['percentage'] for m in member_scores) / len(member_scores)
    print(f"\nGroup Average: {avg_score:.1f}%")
    if avg_score >= 80:
        print("Exceptional group performance!")
    elif avg_score >= 60:
        print("Solid team effort!")
    else:
        print("Keep studying together - improvement comes with practice!")
    print("\n" + "="*60 + "\n")
def display_enhanced_menu():
    """Display enhanced main menu"""
    print("="*60)
    print("MAIN MENU")
    print("="*60)
    print("1. Add study session")
    print("2. View group statistics")
    print("3. Show global leaderboard")
    print("4. Get motivation")
    print("5. Take group quiz")
    print("6. View recent activity")
    print("7. Compare two groups")
    print("8. Export group report")
    print("9. Exit")
    print("="*60)
def main():
    """Enhanced main program loop"""
    print("\n" + "="*60)
    print("COMPLETE GROUP STUDY ASSISTANT")
    print("Week 1 Final Project - Enhanced Edition")
    print("="*60)
    print("\nWelcome! This tool helps study groups track progress,")
    print("stay motivated and learn together.\n")
    while True:
        try:
            display_enhanced_menu()
            choice = get_valid_number("\nYour choice (1-9): ", 1, 9)
            if choice == 1:
                add_study_session()
            elif choice == 2:
                group_name = get_non_empty("\nEnter group name: ")
                view_group_stats(group_name)
            elif choice == 3:
                show_leaderboard()
            elif choice == 4:
                show_motivation()
            elif choice == 5:
                run_group_quiz()
            elif choice == 6:
                view_recent_activity()
            elif choice == 7:
                compare_groups()
            elif choice == 8:
                group_name = get_non_empty("\nEnter group name to export: ")
                export_group_report(group_name)
            else:
                print("\n" + "="*60)
                print("Thank you for using Group Study Assistant!")
                print("Keep learning together!")
                print("="*60 + "\n")
                break
        except KeyboardInterrupt:
            print("\n\nExiting safely...\n")
            break
        except Exception as e:
            print(f"\nAn error occured: {e}")
            print("Please try again.\n")
def view_recent_activity():
    """Show the 10 most recent sessions across all groups"""
    sessions = load_all_sessions()
    if not sessions:
        print("\n No activity yet!\n")
        return
    print("\n" + "="*70)
    print("RECENT ACTIVITY (Last 10 sessions)")
    print("="*70 + "\n")
    for session in sessions[-10:]:
        print(f"[{session['timestamp']}]")
        print(f"{session['group']} - {session['member']}")
        print(f"{session['subject']} ({session['hours']}hrs, {session['difficulty']})")
    print("="*70 + "\n")
def compare_groups():
    """Compare statistics between two groups"""
    print("\n--- GROUP COMPARISON ---\n")
    group1 = get_non_empty("First group name: ")
    group2 = get_non_empty("Second group name: ")
    sessions1 = [s for s in load_all_sessions() if s["group"] == group1]
    sessions2 = [s for s in load_all_sessions() if s["group"] == group2]
    if not sessions1:
        print(f"\nNo data for {group1}\n")
        return
    if not sessions2:
        print(f"\nNo data for {group2}\n")
        return
    print("\n" + "="*70)
    print(f"{group1.upper()} vs {group2.upper()}")
    print("="*70 + "\n")
    stats = {}
    for name, sessions in [(group1, sessions1), (group2, sessions2)]:
        total_hours = sum(s["hours"] for s in sessions)
        avg_mood = sum(s["mood"] for s in sessions) / len(sessions)
        num_members = len(set(s["member"] for s in sessions))
        stats[name] = {
            "sessions": len(sessions),
            "hours": total_hours,
            "members": num_members,
            "mood": avg_mood,
            "hours_per_member": total_hours / num_members
        }
    print(f"{'Metric':<25} {group1:<20} {group2:<20}")
    print("-" * 70)
    print(f"{'Total Sessions':<25} {stats[group1]['sessions']:<20} {stats[group2]['sessions']:<20}")
    print(f"{'Total Hours':<25} {stats[group1]['hours']:<20.1f} {stats[group2]['hours']:<20.1f}")
    print(f"{'Active Members':<25} {stats[group1]['members']:<20} {stats[group2]['members']:<20}")
    print(f"{'Hours per Member':<25} {stats[group1]['hours_per_member']:<20.1f} {stats[group2]['hours_per_member']:<20.1f}")
    print(f"{'Avg Motivation':<25} {stats[group1]['mood']:<20.1f} {stats[group2]['mood']:<20.1f}")
    print("\n" + "="*70 +"\n")
def export_group_report(group_name):
    """Export a detailed report for a group to a text file"""
    sessions = [s for s in load_all_sessions() if s["group"] == group_name]
    if not sessions:
        print(f"\nNo data for {group_name}\n")
        return
    filename = f"{group_name.replace(' ', '_')}_report.txt"
    try:
        with open(filename, "w") as file:
            file.write("="*70 + "\n")
            file.write(f"STUDY GROUP REPORT: {group_name.upper()}\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            file.write("="*70 + "\n\n")
            total_hours = sum(s["hours"] for s in sessions)
            members = set(s["member"] for s in sessions)
            avg_mood = sum(s["mood"] for s in sessions) / len(sessions)
            file.write("SUMMARY\n")
            file.write("-" * 70 + "\n")
            file.write(f"Total Sessions: {len(sessions)}\n")
            file.write(f"Total Hours: {total_hours:.1f}\n")
            file.write(f"Active Members: {len(members)}\n")
            file.write(f"Average Motivation: {avg_mood:.1f}/10\n\n")
            file.write("MEMBER BREAKDOWN\n")
            file.write("-" * 70 + "\n")
            member_data = {}
            for session in sessions:
                member = session["member"]
                if member not in member_data:
                    member_data[member] = []
                member_data[member].append(session)
            for member, member_sessions in sorted(member_data.items()):
                member_hours = sum(s["hours"] for s in member_sessions)
                member_avg_mood = sum(s["mood"] for s in member_sessions) / len(member_sessions)
                file.write(f"\n{member}:\n")
                file.write(f"Sessions: {len(member_sessions)}\n")
                file.write(f"Total Hours: {member_hours:.1f}\n")
                file.write(f"Avg Motivation: {member_avg_mood:.1f}/10\n")
            file.write("\nDETAILED SESSION LOG\n")
            file.write("-" * 70 + "\n\n")
            for session in sessions:
                file.write(f"[{session['timestamp']}]\n")
                file.write(f"Member: {session['member']}\n")
                file.write(f"Subject: {session['subject']}\n")
                file.write(f"Hours: {session['hours']}\n")
                file.write(f"Difficulty: {session['difficulty']}\n")
                file.write(f"Motivation: {session['mood']}\n")
                file.write(f"Notes: {session['notes']}\n\n")
            file.write("="*70 + "\n")
            file.write("End of Report\n")
        print(f"\nReport exported to '{filename}'\n")
    except Exception as e:
        print(f"\nError creating report: {e}\n")
if __name__ == "__main__":
    main()