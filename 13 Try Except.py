a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

try:
    print("The sum of the numbers is:", int(a)+int(b))

except Exception as e:
    print(e)

print("This is an important line")
