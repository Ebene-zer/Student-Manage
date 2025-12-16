"""
This file have the solution implemented using the procedural paradigm
"""

#Welcome message
print("=" * 5 + " Hello! Welcome To Fuachie Student Manage. " + "=" * 5 )

# Create a list to store student details in dictionaries
student_list= []

# Take student details (Use a loop to get user input repeatedly)
while True:
    option = input("Enter: 'Add' (to add Student) | 'Q' (to quit): ")
    student_data = {} # An empty dictionry for each entery
    
    if option.lower() == 'add':
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
        student_list.append(Student_ID)
        student_list.append(name)
        student_list.append(age)
        student_list.append(residential_status)
        student_list.append(hall_of_residence)
        print("Student Added Successfully!\n") # Give feedback upon a successful add
    elif option.lower() == 'q':
        print("Good bye!")
        break

# # Print to user details of the added student
# print("=" * 5 + " Student Details " + "=" * 5)
# print("Student ID: " + student_list[0])
# print("Name: " + student_list[1])
# print("Age: " + student_list[2])
# print("Border: " + student_list[3])
# print("Hall of Residence: " + student_list[4])

"""
Next:
1. Exception Handling
2. Search student
3. Update student
4. Delete student
5. Optmize code where needed
"""

