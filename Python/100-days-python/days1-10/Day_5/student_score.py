student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199]

total_exam_score = sum(student_score)


max = 0
for score in student_score:
    if score > max:
        max = score

print(max)