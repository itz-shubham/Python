# var = 50
# print("Enter a number less than 50")
#
# number = int(input())
#
# if number < 50:
#     print("Yes, your number is less than 50")
# elif number == 50:
#     print("You entered 50. So it is not a greater number nor lesser")
# else:
#     print("No, your number is greater than 50")


numbers = [6, 12, 3, 15, 1, 31, 4, 7, 54, 5, 83, 21, 2]
print("Enter a number from this list:", numbers)

num = int(input())

if num in numbers:
    print("Yes, its present in list")
if num not in numbers:
    print("You entered a wrong number")




