import os

print(" STUDENT INFORMATION SYSTEM ")
print("-----------------------------------\n")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA - Add information\nB - Record\nC - Search a Record\nD - Delete a Record\nE - Exit Program")

    choice = input("your choice --> ").lower()

    if choice == 'a':
        os.system('cls')
        print("ADDING STUDENT INFORMATION")
        print("-------------------------------")
        student_id = input("Key search for this student use this pattern(course-IDNO) --> ")

        first_name = input("Enter Student First Name --> ").upper()
        Last_name = input("Enter Student Last Name --> ").upper()
        course = input("Enter Student course --> ").upper()
        email = input("Enter student email address --> ")
        isSingle = input("Are you single (True or False) --> ")

        student_records = {student_id : [first_name, Last_name, course, email, isSingle ]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        print("PRINTING STUDENT RECORD")

        for id, record in student_records.items():
            print(f"STUDENT ID {id} in STUDENT RECORD {record}")

        continue

    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        print("============================")

        search_id = input("Enter id to search -> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("===============================")
                print("\n\nRECORD FOUND")
                print("===============================")
                # print the record of search student
                for i in student_records[search_id]:
                    print(f"-- {i}")
            else:
                print("===============================")
                print("\n\nNO RECORD FOUND")
                print("===============================")

        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETING EXISTING RECORD")

        search_id = input("Enter id to search -> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("===============================")
                print("\n\nRECORD FOUND")
                print("===============================")
                # print the record of search student
                for i in student_records[search_id]:
                    print(f"-- {i}")

            student_records.pop(search_id)
            print("RECORD DELETED")
        else:
            print("===============================")
            print("\n\nNO RECORD FOUND")
            print("===============================")

        continue
    elif choice == 'e':
        print("System Exit")
        break
    else:
        print("\nINVALID CHOICE, please RE-ENTER YOUR CHOICE ")
        choice
