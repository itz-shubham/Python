f = open("file.txt")

f.seek(10)
print(f.tell())
print(f.readline())

# print(f.tell())
print(f.readline())

# print(f.tell())
f.close()
