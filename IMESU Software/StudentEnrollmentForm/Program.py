import sys


# Initialize global variables
firstName = ""
lastName = ""
section = ""
age = 0
NewSection = ""
idNum = ""
SectionNineDisplay = ['Bacolod', 'Borongan', 'Calbayog', 'Catarman', 'Dumagete', 'Kalibo', 'Maasin', 'Romblon', 'San Carlos']
SectionTenDisplay = ['Butuan', 'Digos', 'Dipolog', 'Iligan', 'Ipil', 'Mati', 'Surigao']
StudentTable = []
# Constants for tuition fees
TUITION_9TH_GRADE = 71000
TUITION_10TH_GRADE = 69000

# Code Area
def InitiateSections(section):
    if section in SectionNineDisplay:
        return SectionNineDisplay.index(section)
    elif section in SectionTenDisplay:
        return SectionTenDisplay.index(section)
    else:
        return -1 

def SectionSet():
    print("[To Access the List of Sections, Type 'display' to show all sections ]")
    section = input("\nEnter your desired section: ")
    if section.lower() == "display":
        PrintSection()
        return SectionSet()
    
    index = InitiateSections(section)
    if index != -1:
        #DEVELOPER OPTION: TO DISPLAY THE SECTION NUMBER
        #Comment out these 2 lines below if needed.
        print(f"DEV: The index of '{section}' is: {index}")
        return section
    else:
        print("Section not found. Please enter a valid section.")
        return SectionSet()

def PrintSection():
    print("\nSections:")
    print("------------------------------------------------")
    print(f"{'Ninth Grade':<15}{'Tenth Grade':<15}")
    print("------------------------------------------------")
    max_length = max(len(SectionNineDisplay), len(SectionTenDisplay))
    for i in range(max_length):
        sec = SectionNineDisplay[i] if i < len(SectionNineDisplay) else ''
        sect = SectionTenDisplay[i] if i < len(SectionTenDisplay) else ''
        print(f"{sec:<15} {sect:<15}")

def InitAge():
    global age  # Declare age as global to modify it
    age = int(input("Enter age: "))  # Store the age in the global variable
    return age

def Enrollment():
    while True:
        student_Info = {}
        student_Info['firstName'] = input("Enter your First Name: ")
        student_Info['lastName'] = input("Enter your Last Name: ")
        student_Info['section'] = SectionSet()
        student_Info['age'] = InitAge()
        student_Info['idNum'] = input("Enter your ID Number [##-####]: ")
        StudentTable.append(student_Info)
        another = input("Do you want to add another student? (yes/no): ").strip().lower()
        if another != 'yes':
            Terminal()
            break  # Exit the loop and return to the terminal
        
def DisplayEnrolleeTable():
    print("\nStudent Record:")
    print("------------------------------------------------")
    print(f"{'First Name':<15}{'Last Name':<15}{'Section':<10}{'Age':<5}{'ID Number':<10}")
    print("------------------------------------------------")
    
    for record in StudentTable:
        print(f"{record['firstName']:<15}{record['lastName']:<15}{record['section']:<10}{record['age']:<5}{record['idNum']:<10}")

def main():
    print('Welcome To The Improved Modular Enrollment System Utility [IMESU]')

def ViewStudentById():
    idNum_to_search = input("Enter the ID Number of the student you want to view: ")
    
    # Search by idNum
    for record in StudentTable:
        if record['idNum'] == idNum_to_search:
            print("\nStudent Information:")
            print("------------------------------------------------")
            print(f"First Name: {record['firstName']}")
            print(f"Last Name: {record['lastName']}")
            print(f"Section: {record['section']}")
            print(f"Age: {record['age']}")
            print(f"ID Number: {record['idNum']}")
            return Terminal()
        
    print("Student with ID Number '{}' not found.".format(idNum_to_search))
    ViewStudentById()
def UpdateStudent():
    idNum_to_update = input("Enter the ID Number of the student you want to update: ")
    
    # IdNum Search
    for record in StudentTable:
        if record['idNum'] == idNum_to_update:
            print("\nStudent Information:")
            print("------------------------------------------------")
            print(f"First Name: {record['firstName']}")
            print(f"Last Name: {record['lastName']}")
            print(f"Section: {record['section']}")
            print(f"Age: {record['age']}")
            print(f"ID Number: {record['idNum']}")
            print("------------------------------------------------")

            # Mini terminal for updating
            while True:
                print("\nWhat would you like to update?")
                print("[1. First Name]")
                print("[2. Last Name]")
                print("[3. Section]")
                print("[4. Age]")
                print("[5. ID Number]")
                print("[6. Confirm and Exit]")
                
                choice = input("Enter the number of your choice: ")
                match choice:
                    case '1':
                        new_first_name = input("Enter new First Name: ")
                        record['firstName'] = new_first_name

                        print("\nStudent Information:")
                        print("------------------------------------------------")
                        print(f"First Name: {record['firstName']}")
                        print(f"Last Name: {record['lastName']}")
                        print(f"Section: {record['section']}")
                        print(f"Age: {record['age']}")
                        print(f"ID Number: {record['idNum']}")
                        print("------------------------------------------------")
                    case '2':
                        new_last_name = input("Enter new Last Name: ")
                        record['lastName'] = new_last_name

                        print("\nStudent Information:")
                        print("------------------------------------------------")
                        print(f"First Name: {record['firstName']}")
                        print(f"Last Name: {record['lastName']}")
                        print(f"Section: {record['section']}")
                        print(f"Age: {record['age']}")
                        print(f"ID Number: {record['idNum']}")
                        print("------------------------------------------------")
                    case '3':
                        new_section = SectionSet()  # Reuse SectionSet to get a valid section
                        record['section'] = new_section
                        print("\nStudent Information:")
                        print("------------------------------------------------")
                        print(f"First Name: {record['firstName']}")
                        print(f"Last Name: {record['lastName']}")
                        print(f"Section: {record['section']}")
                        print(f"Age: {record['age']}")
                        print(f"ID Number: {record['idNum']}")
                        print("------------------------------------------------")
                    case '4':
                        new_age = InitAge()  # Reuse InitAge to get a valid age
                        record['age'] = new_age
                        print("\nStudent Information:")
                        print("------------------------------------------------")
                        print(f"First Name: {record['firstName']}")
                        print(f"Last Name: {record['lastName']}")
                        print(f"Section: {record['section']}")
                        print(f"Age: {record['age']}")
                        print(f"ID Number: {record['idNum']}")
                        print("------------------------------------------------")
                    case '5':
                        new_id_num = input("Enter new ID Number [##-####]: ")
                        record['idNum'] = new_id_num
                        print("\nStudent Information:")
                        print("------------------------------------------------")
                        print(f"First Name: {record['firstName']}")
                        print(f"Last Name: {record['lastName']}")
                        print(f"Section: {record['section']}")
                        print(f"Age: {record['age']}")
                        print(f"ID Number: {record['idNum']}")
                        print("------------------------------------------------")
                    case '6':
                        print("Update confirmed.")
                        return  Terminal()# Exit the update loop
                    case _:
                        print("Invalid choice. Please try again.")
            return
    
    print("Student with ID Number '{}' not found.".format(idNum_to_update))

def enrollStudent():
    id_num = input("Enter the ID Number of the student: ")
    
    # Search for the student in the StudentTable
    for student in StudentTable:
        if student['idNum'] == id_num:
            full_name = f"{student['firstName']} {student['lastName']}"
            section = student['section']
            # Determine tuition fee based on section
            if section in SectionNineDisplay:
                tuition_fee = TUITION_9TH_GRADE
            elif section in SectionTenDisplay:
                tuition_fee = TUITION_10TH_GRADE
            else:
                tuition_fee = 0  # Default case, should not happen
            
            print(f"\nStudent Information:")
            print(f"Full Name: {full_name}")
            print(f"ID Number: {id_num}")
            print(f"Tuition Fee: P{tuition_fee}")
            return Terminal()  # Exit the function after displaying the information

    print("Student with ID Number not found.")
    enrollStudent()


def Terminal():
    while True:  # Loop until the user decides to exit
        print("\n+=TERMINAL=+")
        print("=============================================")
        print("[1. Add Student]")
        print("[2. Display Student Table]")
        
        # Check if StudentTable is empty
        if not StudentTable:
            print("[3. View Student Information (Unavailable)]")
            print("[4. Update Student Information (Unavailable)]")
            print("[5. Enroll Student (Unavailable)]")
        else:
            print("[3. View Student Information]")
            print("[4. Update Student Information]")
            print("[5. Enroll Student]")  # Option to enroll a student
        
        print("[6. Exit]")  # Option to exit
        answer = input("Enter the number of your choice: ")
        match answer:
            case '1':
                Enrollment()
            case '2':
                DisplayEnrolleeTable()
            case '3':
                if StudentTable:  # Check if there are students to view
                    ViewStudentById()
                else:
                    print("No students available to view.")
            case '4':
                if StudentTable:  # Check if there are students to update
                    UpdateStudent()
                else:
                    print("No students available to update.")
            case '5':
                if StudentTable:  # Check if there are students to enroll
                    enrollStudent()  # Call the enrollStudent function
                else:
                    print("No students available to enroll.")
            case '6':
                print("Thank you for using IMESU, That In All Things, God May Be Glorified!")
                return exit()# Exit the terminal loop
            case _:
                print("Invalid choice. Please try again.")
# This is the Function Area, All def functions will be executed here.
# main is the master function and is responsible for displaying the program.

main()
Terminal()


#Enrollment app will use IO (for taking user input)
# all data will be sent to an array[] that will store all the main data.
# to which the array will be arranged and sorted using different parameters.
# then using specific commands (switch case) the user will be able to do different functionalities on the data

# Sample Commands

"""
    Enroll
        - Opens the Enroll Class, the enroll class has the instrutions of:
        ."What is your first name?:" (Input [firstName] Variable)[/]
        ."What is your last name?;" (Input [lastName] Variable)[/]
        ."What is your intended section?;" (Input[Section] Variable)
        ."How old are you?;" (Input [age] Variable)
        .Display the student record in the console[/]
        .""
"""