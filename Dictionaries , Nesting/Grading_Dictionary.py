student_scores = {
  "Harsha": 81,
  "Nani": 78,
  "Kane": 99, 
  "Stokes": 74,
  "Mehta": 62,
}

for key in student_scores:

    if student_scores[key] > 91:
        student_scores[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_scores[key] = "Very Good"
    elif student_scores[key] > 70:
        student_scores[key] = "Good"
    else:
        student_scores[key] = "Fail"

print(student_scores)