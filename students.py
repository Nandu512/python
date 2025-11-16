frontend={"raju","sreehari","binu"}
backend={"balan","arjun","kohili","raju"}
backend.add('tony')
print('updated backend students:',backend)
remove=frontend.pop()
print('updated frontend students:',frontend)
print('combined list of all students',frontend|backend)
print('Displaying the list of students who are enrolled only in Backend, but not in Frontend',backend-frontend)
print('Displaying the total number of unique students',frontend^backend)
course={
    "frontend":len(frontend),
    "backend":len(backend)
}
for x,y in course.items():
    print(x,y)
full_stack={
    **course,
    "fullstack":course["frontend"]+course["backend"]
}
print(full_stack)