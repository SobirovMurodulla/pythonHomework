import csv
from collections import defaultdict

grades = []
with open('grades.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)

subject_grades = defaultdict(list)
for grade in grades:
    subject_grades[grade['Subject']].append(grade['Grade'])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Write the average grades to average_grades.csv
with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, avg_grade])