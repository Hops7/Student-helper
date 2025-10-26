group_members = ["Jordano", "Alexandriano", "Patriko", "Casey"]
study_hours = [2, 1.5, 3, 1]

print(group_members[0])
print(f"Your group has {len(group_members)} members")

group_members.append("Riley")
study_hours.append(2.5)

print(f"You obtained a new study gruppe member!Now ya got {len(group_members)} members")

for member in group_members:
    print(f"- {member}")

group_session = {
    "group_name": "Kocicaci",
    "subject": "Mathematics",
    "date": "2025-01-01",
    "total_hours": 10,
    "members_present": 4
}

print(f"Group: {group_session['group_name']}")
print(f"Subject: {group_session['subject']}")
print(f"Total study time: {group_session['total_hours']} hours")

group_session["total_hours"] = 12
group_session["notes"] = "Gute session!! Everybody participated."

all_sessions = [
    {"date": "2025-01-01", "subject": "Law", "hours": 10},
    {"date": "2025-01-02", "subject": "Mathematics", "hours": 8}
]

for session in all_sessions:
    print(f"{session['date']}: {session['subject']} - {session['hours']} hrs")
