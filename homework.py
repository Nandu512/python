student=int(input("enter the no of students to add:"))
try:
    print("existing student list are")
    with open("students.txt","r")as file:
        print(file.read())
except FileNotFoundError:
    print("not existing file found..new file will be created")
    with open("student.txt","a") as file:
        for x in range(student):
            name=input("enter the name:")
            file.write(name+"\n")
print("updated list of students are:")
with open("students.txt","r") as file:
    print(file.read())
            
            
    
