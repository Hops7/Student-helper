print("=== SAFE INPUT PRACTICE ===\n")
print("Example 1: Handling number input")
try:
    hours = float(input("How many hours did you study?"))
    print(f"Great! You studied {hours} hours!\n")
except ValueError:
    print("That's not a valid number!\n")
print("Example 2: Keep asking until valid")
while True:
    try:
        members = int(input("How many members in your group?"))
        if members <= 0:
            print("Must be 1+ members!")
            continue
        print(f"Got it! {members} members\n")
        break
    except ValueError:
        print("Please enter a whole number!")
print("Example 3: Safe file reading")
filename = input("Enter filename to read:")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"File contents: \n{content}\n")
except FileNotFoundError:
    print(f"File '{filename}' not found!\n")
print("Example 4: Multiple error types")
try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    result = num1 / num2
    print(f"Result: {result}\n")
except ValueError:
    print("Please enter valid numbers!\n")
except ZeroDivisionError:
    print("Cannot divide by zero!\n")
print("Example 5: Safe list access")
members = ["Alex", "Jordan", "Sam"]
try:
    index = int(input(f"Enter member number (1-{len(members)}): "))
    print(f"Member {members[index - 1]}\n")
except (ValueError, IndexError):
    print("Invalid member number!\n")
print("=== PRACTICE COMPLETE ===")