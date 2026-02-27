student_records = []

for student_data_input in range(1,3,1):
    student_name = input(f"Student {student_data_input}'s name: ")
    student_grade = input(f"Student {student_data_input}'s grade: ")
    student_subject = input(f"Student {student_data_input}'s grade for which subject: ")

    students_data_summary = (student_name, student_grade, student_subject)
    student_records.append(students_data_summary)

print(student_records)
