# f = open("test.txt", "a")
# # f.write("Python is an interpreted, high-level and general-purpose programming language.")
#
# # f.write("Python is an interpreted, high-level and general-purpose programming language.\n")
#
# a = f.write("Python is an interpreted, high-level and general-purpose programming language.\n")
# print(a)

# ### Handle read and write both
f = open("test.txt", "r+")
print(f.read())
f.write(".")

f.close()
