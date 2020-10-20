class Programmers:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = f"{first_name}@{last_name}.com"

    def full_name(self):
        return f"Name: {self.first_name} {self.last_name}"

    @property
    def email(self):
        if self.first_name is None or self.last_name is None:
            return "Email is not set. You can set email using setter"

        return f"{self.first_name}@{self.last_name}.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.first_name = names.split("_")[0]
        self.last_name = names.split("_")[1]

    @email.deleter
    def email(self):
        self.first_name = None
        self.last_name = None


# harry = Programmers("Code with", "Harry")
shubham = Programmers("shubham", "kumar")

print(shubham.full_name())
# print(shubham.email())

# shubham.last_name = "Coder"
# print(shubham.email)  # This will cannot change the name. For this we have to create a function

print(shubham.email)
shubham.last_name = "Coder"
print(shubham.email)

shubham.email = "shubham_kumar@gmail.com"
print(shubham.full_name())
print(shubham.email)

del shubham.email
print(shubham.email)
