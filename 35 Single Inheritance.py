class Employee:
    no_of_leaves = 8

    def __init__(self, a_name, a_salary, a_role):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print("This is good " + string)


class Programmer(Employee):

    def print_programmer(self):
        return f"The name is {self.name}.\nSalary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")
karan = Employee.from_dash("Karan-480-Student")

shubham = Programmer("Shubham", 100, "Flutter Programmer")
rohan = Programmer("Rohan", 500, "Python Programmer")

print(shubham.print_programmer())
