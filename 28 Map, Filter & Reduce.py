# ------------------------- Map -------------------------

# numbers = ["3", "84", "54", "64"]
#
# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])
# # Or,
#
# numbers = list(map(int, numbers))
#
# numbers[3] = numbers[3] + 1
# print(numbers[3])

#
# # def sq(a):
# #     return a * a
# #
#
# num = [64, 3, 15, 2, 21, 5, 54, 13, 2, 1, 31, 6, 4, 7]
# # square = list(map(sq, num))
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a * a
#
#
# def cube(a):
#     return a * a * a
#
#
# calculate = [square, cube]
#
# for i in range(5):
#     val = list(map(lambda x: x(i), calculate))
#     print(val)


# ------------------------- Filter -------------------------

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def is_greater_than_5(num):
#     return num > 5
#
#
# greater_than_5 = list(filter(is_greater_than_5, list_1))
# print(greater_than_5)


# ------------------------- Reduce -------------------------
from functools import reduce

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i = total = 0
# for item in list_1:
#     total = total + list_1[i]
#     i += 1

total = reduce(lambda x, y: x + y, list_1)
print(total)
