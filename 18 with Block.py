# f = open("file.txt")
#
# a = f.read(6)
# print(a)
#
# f.close()

with open("file.txt") as f:
    a = f.read(6)
    print(a)
