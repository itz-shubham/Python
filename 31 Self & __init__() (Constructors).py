class Employee:
    no_of_leave = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role  # we inserting the name arguments into self.name

    def print_details(self):
        return f"Name: {self.name}\nSalary: {self.salary}\nRole: {self.role}"


shubham = Employee("Shubham", 0, "Intern")  # this arguments is going to: def __init__(self, name, salary, role):
harry = Employee("Harry", 400, "Instructor")

# shubham.name = "Shubham"
# shubham.salary = 0
# shubham.role = "Intern"
#
# harry.name = "Harry"
# harry.salary = 400
# harry.role = "Instructor"

# print(harry.salary)
print(shubham.print_details())
