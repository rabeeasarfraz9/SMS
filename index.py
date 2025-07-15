class studentManagement:
  def __init__(self):
    self.students=[]

  def add_student(self):
    name= input("Enter Student's Name:\n")
    roll_no= input("Enter Roll_No:\n")
    course= input("Enter Course:\n")
    student= {'name': name, 'roll_no': roll_no, 'course': course}
    self.students.append(student)
    print("Added Student Successfully\n")


  def search_student(self):
    keyword= input("Enter Name or Roll-No to Search: ")
    for student in self.students:
            if student['name']== keyword or student['roll_no']== keyword:
                print(f"Found: Name: {student['name']}, Roll-No: {student['roll_no']}, Course: {student['course']}")

            else:
                print("Student not Found.")

  def del_student(self):
     Rno= input("Enter Roll-No of a student you want to delete: ")
     for student in self.students:
            if student['roll_no']== Rno:
               self.students.remove(student)
               print("Student Record Deleted")

            else:
               print("Student not Found")   

  def view_student(self):
    if not self.students:
        print("No Student Found.")
    else:
         for i, student in enumerate(self.students, start=1):
              print(f"{i}. Name: {student['name']}, Roll-No: {student['roll_no']}, Course: {student['course']}")


def main():
    s=studentManagement()          
    while True:

     print("Student Management System\n") 
     print("1. Add Student\n")
     print("2. View Students\n")
     print("3. Search Student\n")
     print("4. Delete Student\n")
     print("5. Exit")
     choice=input("Choose one of the above option 1-5: ")
    
     if choice == '1':
      s.add_student()

     elif choice =='2':
        s.view_student()

     elif choice =='3':
        s.search_student()

     elif choice == '4':
        s.del_student()
    
     elif choice=='5':
        print("Exiting...")
        break

     else:
        print("Invalid Choice.")    

if __name__=="__main__":

     main()        
         
     


