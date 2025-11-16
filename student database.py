python={"raju","sreehari","binu"}
data_science={"balan","arjun","kohili","raju"}
python.add('abhi')
print('updated list of python is:',python)
remove=data_science.pop()
print('updated list of data science is:',data_science)
print('students who enrolled in both courses' ,python & data_science)
print('students only in python not in data science' ,python-data_science)
print('combined list of all students',python|data_science)
course={
     "python":3,
     "data_science":4
     
    
}
for x,y in course.items():
    print(x,y)
    double={key:value*2 for key,value in course.items()}
    print(double)