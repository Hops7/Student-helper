import random


quotes = [
    "Every business starts small, but growth is exponentially increasing",
    "You're securing your future so do something for it",
    "The earlier you start the sooner you'll achieve financial freedom",
    "Starting also means progress",
    "Keep up the motivation!"
]

group_name = input("Whats ya grupz name fellas?")

while True:
    num_members = input("How many of you are there?")
    try:
    
         num_members = float(num_members)
         if num_members < 0:
             print("0-+infinity answers only(inf not included)")
         else:
             break
    except ValueError:
        print("Bruda enter a valid number!")
print(f"You entered: {num_members}")

while True:
    subject_answer = input("What do you want to study today? ")
    if subject_answer.replace(" ", "").isalpha() and subject_answer.strip():
        subject = subject_answer
        break
    else:
        print("Only words/letters bruda")


while True:
    hours_planned = input("How many hrs does each of you intend to study?")
    try:
         hours_planned = float(hours_planned)
         if hours_planned < 0:
             print("0-+infinity answers only(inf not included)")
         else:
             break
    except ValueError:
        print("Bruda enter a valid number!")
print(f"You entered: {hours_planned}")

total_group_hours = hours_planned * num_members

random_number = random.randint(0, 4)
random_quote = quotes[random_number]

print("\n" + "="*60)
print(f"Hey {group_name}!^^")
print(f"Group size: {num_members}")
print(f"Today's focus: {subject}")
print(f"Individual commitment: {hours_planned} hours per person")
print(f"Total group effort: {total_group_hours} hours combined!")
print(f"\nRemember: {random_quote}")
print("=" *60)