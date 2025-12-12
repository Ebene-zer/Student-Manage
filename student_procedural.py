"""
This file have the solution implemented using the procedural paradigm
"""

#Welcome message
print("=" * 5 + " Hello! Welcome To Fuachie Student Manage. " + "=" * 5)

# Create a list to store student details
student = []

# Take student details as input 
Student_ID = input("Enter Student ID: ")
name = input("Enter Student name: ")
age = input("Enter student age: ")
residential_status = input("Boarder?: Y/N (Enter Y for Yes and N for No).")
hall_of_residence = "N/A"
if residential_status.lower() == "y":
    hall_of_residence = input("Enter hall of residence: ")
else:
    print(hall_of_residence)

# Now add (in this case append) student data to the student list
student.append(Student_ID)
student.append(name)
student.append(age)
student.append(residential_status)
student.append(hall_of_residence)
print("Student Added Successfully!\n") # Give feedback upon a successful add


# Print to user details of the added student
print("=" * 5 + " Student Details " + "=" * 5)
print("Student ID: " + student[0])
print("Name: " + student[1])
print("Age: " + student[2])
print("Border: " + student[3])
print("Hall of Residence: " + student[4])


