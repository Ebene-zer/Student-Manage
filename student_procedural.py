"""
This file have the solution implemented using the procedural paradigm
"""

#Welcome message
print("=" * 5 + " Hello! Welcome To Fuachie Student Manage. " + "=" * 5 )

# Create a list to store student details in dictionaries
student_list = []

def search_for_student(query, list_of_students): # The search function
    search_results = []
    for data in list_of_students:
        if query in data['name'].lower(): # Check if the query is in student's name (case-insensitive)
            search_results.append(data)
        # Or check if the query matches the student's ID
        elif query in data['student_ID']:
            search_results.append(data)
    return search_results


def update_student():
    pass

def delete_student():
    pass


# Take student details (Use a loop to get user input repeatedly)
while True:
    option = input("Enter: 'Add' (to add Student) | 'Search' (to search for student) | 'Q' (to quit): ")

    if option.lower() == 'q':
        print("Good bye!")
        break
    elif option.lower() == 'add':
        student_data = {} # An empty dictionry for each entery

        student_ID = input("Enter Student ID: ")
        name = input("Enter Student name: ")
        age = input("Enter student age: ")
        residential_status = input("Boarder? Y/N (Enter Y for Yes and N for No): ")
        hall_of_residence = "N/A"
        if residential_status.lower() == "y":
            hall_of_residence = input("Enter hall of residence: ")
        

        # Assign the inputs to dictionary keys
        student_data['student_ID'] = student_ID
        student_data['name'] = name
        student_data['age'] = age
        student_data['residential_status'] = residential_status
        student_data['hall_of_residence'] = hall_of_residence

        # Append the populated dictionary to the list
        student_list.append(student_data)
        print("Student Added Successfully!\n") # Give feedback upon a successful add

        # Print to user details of the added student
        print("=" * 5 + " Student Details " + "=" * 5)
        for student in student_list:
            #Use .get() (returns None or a specified default if the key is not found)
            print(f"Student ID: {student.get('student_ID', "Not Found")}")
            print(f"Name: {student.get('name', "Not Found")}")
            print(f"Age: {student.get('age', "Not Found")}")
            print(f"Residential Status: {student.get('residential_status', "Not Found")}")
            print(f"Hall of Residence: {student.get('hall_of_residence', "Not Found")}")
    
    elif option.lower() == "search": 
        search_query = input("Enter student name or ID to search: ").strip().lower() # Search for student
        # call the search function here and pass two agruments (search_query and the student_list)
        found_students = search_for_student(search_query, student_list)
        if found_students:
            print(f"\nFound {len(found_students)} student(s): ")
            for student in found_students:
                print(f"""\nStudent ID: {student['student_ID']}
Name: {student['name']}
Age: {student['age']}
Residential Status: {student['residential_status']}
Hall of Residence: {student['hall_of_residence']}
""")
        else:
            print("\nNo students found macthing your criteria.")

    else:
        print("Invalid input: Choose correction option from the main menu.")
        continue



"""
Next:
1. Exception Handling
2. Search student - Done
3. Update student
4. Delete student
5. Optmize code where needed
"""

