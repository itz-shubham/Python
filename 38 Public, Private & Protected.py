# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Employee:
#     def __init__(self, name, age):
#         self._name = name  # protected attribute
#         self._age = age  # protected attribute
#
#
# class Employee:
#     def __init__(self, name, age):
#         self.__name = name  # private attribute
#         self.__age = age  # private attribute


# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    var = 8
    _protected = 9
    __pr = 98

    def __init__(self, a_name, a_salary, a_role):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @staticmethod
    def print_good(string):
        print("This is good " + string)


emp = Employee("harry", 343, "Programmer")
# print(emp._Employee__pr)
