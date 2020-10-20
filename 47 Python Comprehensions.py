# list1 = []
#
# for number in range(100):
#     if number % 3 == 0:
#         list1.append(number)
#
# print(list1)

# list1 = [number for number in range(100) if number % 3 == 0]
# print(list1)

# dict1 = {number: f"item{number}" for number in range(1, 100) if number % 2 == 0}
# # dict1 = {value: key for key, value in dict1.items()} # This the way we can change the dictionary
# print(dict1)

# dresses = {dress for dress in ["dress1", "dress2", "dress1",
#                                "dress2", "dress1", "dress2"]}
# print(dresses)
# print(type(dresses))

evens = (i for i in range(100) if i % 2 == 0)
# print(evens.__next__())

# for item in evens:
#     print(item)
