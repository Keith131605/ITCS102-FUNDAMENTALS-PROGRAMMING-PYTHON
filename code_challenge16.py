import os

print(" STUDENT INFORMATION SYSTEM ")
print("-----------------------------------\n")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA - Add information\nB - Search a Recvord\nC - Delete a Record\nD - modify a Record\nE - Exit Program")

    choice = input("your choice --> ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("-------------------------------")
        search_code = input("Key search for this student use this pattern(course-IDNO) --> ")

        first_name = input("Enter Student First Name --> ").upper()
        Last_name = input("Enter Student Last Name --> ").upper()
        course = input("Enter Student course --> ").upper()
        email = input("Enter student email address --> ")
        isSingle = input("Are you single (True or False) --> ")

        student_records = {search_code : [first_name, Last_name, course, email, isSingle ]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')
        code = input("input search code --> ")

        for j in student_records.keys():
            if code in student_records.keys():
                print("Record Found")

        os.system('cls')
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("EDITING EXISTING RECORD")
        continue
    elif choice == 'e':
        print("System Exit")
        break
    else:
        print("\nINVALID CHOICE, please RE-ENTER YOUR CHOICE ")
        choice
