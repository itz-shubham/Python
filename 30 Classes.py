class Students:
    std = 11
    pass


shubham = Students()
harry = Students()

shubham.name = "Shubham"
shubham.subjects = ["English", "Maths"]

harry.name = "Harry"
harry.subjects = ["Physics", "Maths"]

# print("Name:", shubham.name, "\nSubjects:", shubham.subjects)

# print(shubham.std)
# print(harry.std)  # Both will share the value
#
# shubham.std = 12  # This will not change the value for all
# print(shubham.std)
# print(harry.std)
#
# Change std for all student we have to change in class variable

Students.std = 12
print(shubham.std)
print(harry.std)
