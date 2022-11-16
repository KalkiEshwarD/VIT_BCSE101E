# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user such as Number of classes held, Number of classes attended and also student medical proof availability [1(for Yes)/0 (for No)].
# Display percentage of class attended and eligibility detail (Allowed/ Not Allowed) for exam.
# If student is having less than 75% but having medical proof, he/she is ‘Allowed’ for exam, otherwise ‘Not Allowed’. 


total_classes = int(input())
classes_attended = int(input())
medical_proof_availability = int(input())

attendance_percentage = ((classes_attended) / (total_classes)) * 100
print(int(attendance_percentage))

if attendance_percentage >= 75.0:
    print("Allowed")
elif attendance_percentage < 75.0 and medical_proof_availability == 1:
    print("Allowed")
else:
    print("Not Allowed")
