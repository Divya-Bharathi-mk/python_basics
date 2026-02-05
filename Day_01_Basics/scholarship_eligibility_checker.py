# Program 4: Scholarship Eligibility
# Concept: Logical Operators (and, or)
Marks = int(input("Enter the mark 0-100: "))
Attendance = int(input("Enter the attendance percentage: "))
if (Marks>=84 and Attendance>=90):
    print ("Your eligible for scholarship")
elif (Marks>=85 or Attendance>=90):
    print ("Not enought, still you eligible for a free fee")
else:
    print ("Your not eligible")
