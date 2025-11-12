with open("study_log.txt", "w") as file:
    file.write("Study Log\n")
    file.write("="*40 + "\n")
    file.write("Day 1: Studied Python -3 total hours\n")

with open("study_log.txt", "a") as file:
    file.write("Session 2: Studied Math - 6 total hours\n")

with open("study_log.txt", "r") as file:
    content = file.read()
    print(content)

print("nReading line by line:")
with open("group_log.txt", "r") as file:
    for line in file:
        print(line.strip())
        