n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

students = {}
for i in range(1, n + 1):
    name = input(f"\nEnter name of student {i}: ").strip() or f"Student_{i}"
    total = 0.0
    for j in range(1, m + 1):
        try:
            total += float(input(f"Enter marks for subject {j}: "))
        except ValueError:
            total += 0.0  # minimal guard: bad input counts as 0
    students[name] = round(total / m, 2)

print("\nStudent Averages (High→Low):")
for name, avg in sorted(students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name}: {avg:.2f}")

best = max(students.values())
toppers = [k for k, v in students.items() if v == best]
print("\nTopper(s): " + ", ".join(toppers) + f" with average {best:.2f}")
print(f"Class average: {sum(students.values()) / len(students):.2f}")
