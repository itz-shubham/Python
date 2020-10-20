# l = 10  # Global
#
#
# def function1(n):
#     # l = 6  # Local
#     # print(n, "The value of l in function is: ", l)
#
#     global l
#     l = l + 5
#     print("Now the value of l is: ", l)
#
#
# function1("...")
#
# print("The value of l is: ", l)

x = 10

def harry():
    x = 20

    def rohan():
        global x
        x = 48
        print("before calling rohan()", x)
        rohan()
        print("after calling rohan()", x)


harry()
print(x)
