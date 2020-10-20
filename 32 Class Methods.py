class Employee:
    no_of_leave = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name: {self.name}\nSalary: {self.salary}\nRole: {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leave = new_leaves


shubham = Employee("Shubham", 0, "Intern")
harry = Employee("Harry", 400, "Instructor")

harry.change_leaves(10)

print(harry.no_of_leave)
