# a = 3
# b = 5
# c = sum((a, b))
# print(c)

def function1(a, b):
    print("Hey I am a function and I am returning:", a + b)


# function1(4, 5)

def function2(a, b):
    """This is a function which is calculating the average of given two number"""
    average = (a + b) / 2
    # print(average)
    return average


print(function2(9, 6))

# print(function2.__doc__)
