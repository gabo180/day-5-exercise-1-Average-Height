# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇\
total = 0
for n in range(0, len(student_heights)):
  total += student_heights[n]
avg = round(total / len(student_heights))
print(avg)

# total_height = 0
# for height in student_heights:
#   total_height += height

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1

# average = round(total_height / number_of_students)
# print(average)

