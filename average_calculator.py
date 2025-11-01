students = {input(f"\nEnter name of student {i+1}: "): 
             sum(float(input(f"Enter marks for subject {j+1}: ")) for j in range(3)) / 3
             for i in range(int(input("Enter number of students: ")))}

print("\nStudent Averages:")
for name, avg in students.items():
    print(f"{name}: {avg:.2f}")

topper = max(students, key=students.get)
print(f"\nTop student is {topper} with average {students[topper]:.2f}")
