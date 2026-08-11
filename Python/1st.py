# Student Report Card Generator

num_students = int(input("Enter the number of students: "))
students = []

for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    student_id = input("ID: ")
    name = input("Name: ")
    
    # Input marks for the three subjects mentioned in your image
    math = float(input("Math Marks: "))
    science = float(input("Science Marks: "))
    english = float(input("English Marks: "))
    
    # Calculations
    marks_list = [math, science, english]
    total = sum(marks_list)
    average = total / len(marks_list)
    
    # Store data in a dictionary
    students.append({
        "id": student_id,
        "name": name,
        "math": math,
        "science": science,
        "english": english,
        "total": total,
        "average": round(average, 2)
    })

# Display Output
print("\nStudent Report Card")
print(f"{'ID':<5} {'Name':<10} {'Math':<8} {'Science':<8} {'English':<8} {'Total':<8} {'Average':<8}")
print("-" * 65)

for s in students:
    print(f"{s['id']:<5} {s['name']:<10} {s['math']:<8} {s['science']:<8} {s['english']:<8} {s['total']:<8} {s['average']:<8.2f}")


student = []
n = int(input("enter the number of students: "))
for i in range(n):
    id =