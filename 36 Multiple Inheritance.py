class Employee:
    no_of_leaves = 8
    var = 8

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


class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The Name is {self.name}. Game is {self.game}"


class CoolProgrammer(Player, Employee):
    language = "C++"

    def print_language(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", ["Cricket"])
# det = karan.print_details()
# karan.print_language()
# print(det)
print(karan.var)
