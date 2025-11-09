def welcome_group():
    print("Welcome to your group stuy session!")

welcome_group()

def greet_group(group_name, num_members):
    print(f"Hello {group_name}!")
    print(f"You have {num_members} members today.")

greet_group("Python hassasinz", 5)
greet_group("Study Esquadro", 3)

def calculate_group_total(hours_list):
    total = 0
    for hours in hours_list:
        total += hours
    return total

member_hours = [2, 3, 1.5, 2.5]
total = calculate_group_total(member_hours)
print(f"Group studied for {total} hours combined!Good job!")

def get_group_performance(total_hours, num_members, sessions):
    avg_per_member = total_hours / num_members
    avg_per_session = total_hours/ sessions

    if avg_per_member >= 3:
        rating = "Perfectoo"
    elif avg_per_member >=2:
        rating = "Good"
    else:
        rating = "Could be better, but you'll catch up!"

    return avg_per_member, avg_per_session, rating

avg_member, avg_session, rating = get_group_performance(20, 4, 3)
print(f"\nGroup Performance: {rating}")
print(f"Average per member: {avg_member} hrs")
print(f"Average per session: {avg_session} hrs")

def display_group_stats(hours_list, group_name):
    total = calculate_group_total(hours_list)
    print(f"\n{group_name} Statistics:")
    print(f"Total hours: {total}")
    print(f"Members: {len(hours_list)}")
    print(f"Average: {total/len(hours_list):.1f} hrs/member")

display_group_stats([2, 3, 2.5, 4], "Study hassasins")