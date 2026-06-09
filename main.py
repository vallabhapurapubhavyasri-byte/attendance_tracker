print("Attendance Management System")
students={}
while True:
  print("\n---Attendance Management System ---")
  print("1. Add Student")
  print("2. Mark Attendance")
  print("3. View Attendance")
  print("4. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    name=input("Enter student name: ")
    students[name]="Not Marked"
    print("Student added successfully")
  elif choice == "2":
    name = input("Enter student name:")
    if name in students:
      status = input("Enter Present/Absent: ")
      students[name]=status
      print("Attendance marked successfully")
    else:
      print("Student not found")
  elif choice == "3":
    print("\nAttendance Recors: ")
    for name, status in students.items():
      print(name, "-", status)
  elif choice == "4":
    print("Exiting....")
    break
  else:
    print("Invalid choice")
