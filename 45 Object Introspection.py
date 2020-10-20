# type(object)
# id(object)
# print(dir(object))
import inspect


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = f"{first_name}.{last_name}@python.com"

    def explain(self):
        return f"This employee is {self.first_name} {self.last_name}"

    @property
    def email(self):
        if self.first_name is None or self.last_name is None:
            return "Email is not set. Please set it using setter"
        return f"{self.first_name}.{self.last_name}@python.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.first_name = names.split(".")[0]
        self.last_name = names.split(".")[1]

    @email.deleter
    def email(self):
        self.first_name = None
        self.last_name = None


employee_1 = Employee("Skill", "F")
# print(employee_1.email)
o = "this is a string"
# print(dir(employee_1))
# print(id("that that"))


print(inspect.getmembers(employee_1))
