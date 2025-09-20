# Task: tuple + while + type()
# 1. Create a tuple with student info
student_info = ("Aya", 19, 3.5, "Computer")  # name, age, GPA, major

# 2. Initialize counter for while loop
i = 0

# 3. While loop to print each element and its type
while i < len(student_info):
    print("Value:", student_info[i], "| Type:", type(student_info[i]))
    i += 1