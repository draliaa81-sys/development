#Initialize a global counter
registration_counter=50000

def student_registration():
    global registration_counter # use the global counter


 # generate the registration id using the current counter value
registration_id = registration_counter
registration_counter += 1 #increment the counter for the next registration

date = input("Enter the registration date (dd/mm/yyyy):")
student_id = input("enter the student id:")
student_name = input("enter the student name:")
course_name = input("enter the course name:")

# display the information
print("/nprinting student registration information:")
print(f"date: {date}")
print(f"student id: {student_id}")
print(f"student name: {student_name}")
print(f"course name: {course_name}")
print(f"registration id: {registration_id}")

# call the function:
student_registration()