students=[]

def add_student():
    name= input("Enter Student's Name:\n")
    roll_no= input("Enter Roll_No:\n")
    course= input("Enter Course:\n")
    student= {'name': name, 'roll_no': roll_no, 'course': course}
    students.append(student)
    print("Added Student Successfully\n")