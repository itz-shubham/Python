
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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))
