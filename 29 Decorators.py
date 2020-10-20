# def function1():
#     print("Hey Shubham")
#
#
# function2 = function1
#
# del function1
# function2()

# def function3(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
#
# a = function3(1)
# print(a)


def dec1(func):
    def execution():
        print("Executing...")
        func()
        print("Task complete!")

    return execution


@dec1
def algebras():
    print("a = b, b = c\n Hence, a = c")


# algebras = dec1(algebras)

algebras()
