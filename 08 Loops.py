# names = [["Ram", 3], ["Shyam", 5], ["Johan", 5], ["Showman", 6]]
#
# # for person, letter_name in names:
# #     print("Total number of letter in", person, "is", letter_name)
#
# d_names = dict(names)
# # print(d_names)
#
# for person in d_names:
#     print(person)
#
# for person, letter_name in d_names.items():
#     print("Total number of letter in", person, "is", letter_name)

garbage = [int, float, 321, 987, 68, 2, "life", 3, 8, 6, 47, "weaving", "ear", 3, 1, 7, 14, 3, 5, 64, 41, 1]

# for items in garbage:
#     if type(items) == int:
#         if items > 6:
#             print(items)

for item in garbage:
    if str(item).isnumeric() and item > 6:
        print(item)


# While loop

i = 0

while i < 20:
    print(i)
    i = i + 1
