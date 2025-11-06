group_total_hours = 15 
num_members = 5
avg_per_member = group_total_hours / num_members

if avg_per_member >- 4:
    print("Good fokin job group!")
elif avg_per_member >= 2:
    print("Good job! Solid group effort detected!")
else:
    print("Keep up the pace!")

members = ["Alex", "Jordan", "Sam", "Casey", "Riley"]

print("\n Individual study times:")
for member in members:
    print(f"- {member}: Please report your hours")

print("\n Attendance:")
for i in range(len(members)):
    print(f"{i+1}. {members[i]}")

subjects = ["Math", "Python"]
study_days = ["Monday", "Wednesday", "Friday"]

print("\n Study schedule")
for subject in subjects:
    for day in study_days:
        print(f"  {subject} on {day}")

sessions_completed = 0
goal = 10
print(f"\n Progress to {goal} sessions:")
while sessions_completed < goal:
    sessions_completed += 1
    print(f"Session {sessions_completed} completed!")
    if sessions_completed>= 3:
        print("... (continuing to goal)")
        break