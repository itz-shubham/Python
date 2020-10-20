# class ParentClass(object):
#     def __init__(self):
#         pass
#
#
# class ChildClass(Parent_Class):
#     def __init__(self):
#         super().__init__()
#

class A:
    class_variable1 = "I am a class variable in class A"

    def __init__(self):
        self.variable1 = "I am inside class A's constructor"
        self.class_variable1 = "Instance variable in class A"
        self.special = "Special"


class B(A):
    class_variable1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.variable1 = "I am inside class B's constructor"
        self.class_variable1 = "Instance variable in class B"


a = A()
b = B()

print(b.special, b.variable1, b.class_variable1)
