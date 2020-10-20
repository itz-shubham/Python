myString = "Shubham is a good boy"
myNumString = "6474681681"
#
# print(myString[8])  # This will print 6th letter
#
# print(myString[0:7])  # This will print 0th letter to 6th letter
#
# print(len(myString))  # This will print length of the variable
#
# print(myString[0:])
# print(myString[:8])
# print(myString[:])
#
# print(myString[0:10:2])  # this will print skipping 1 letter
# print(myString[0:10:3])  # this will print skipping 2 letter
# print(myString[::2])
# print(myString[::])
#
#
# print(myString[-5])  # This will print 5th letter of reversed sentence
# print(myString[::-1])  # This will reverse the sentence


print(myString.isalpha())
print(myNumString.isalnum())
print(myString.endswith("boy"))
print(myString.count("o"))
print(myString.capitalize())  # first letter will be Uppercase
print(myString.lower())
print(myString.upper())
print(myString.replace("Shubham", "He"))
