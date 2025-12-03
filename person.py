class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)  
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)   
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Working Hours: {self.working_hours}, Project: {self.project_name}"
        )


p1 = Person("Reshma", 27)
e1 = Employee("Hari", 26, "20344")
pt1 = PartTime("Anju", 22, 5.5)
c1 = Consultant("Binu", 30, "55678", 4.0, "AI System Upgrade")

p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()