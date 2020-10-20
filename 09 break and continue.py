# i = 0
#
# while True:
#     if i < 8:
#         i = i + 1
#         continue
#
#     print(i+1, end=" ")
#     if i == 50:
#         break  # stop the loop
#     i = i + 1


while True:
    number = int(input("Enter a greater than 100\n"))
    if number > 100:
        print("Congrats you entered a greater number:", number)
        break
    else:
        print("Your number is", number, "try again?")
        continue


# print("Enter a number greater than 100")
# number = int(input())
#
# while number <= 100:
#     print("Your number is", number, "try again?")
#     number = int(input())
#
# print("Congrats you entered a greater number:", number)
