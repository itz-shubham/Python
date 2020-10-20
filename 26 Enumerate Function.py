vegetables = ["Ladyfinger", "Potato", "Chilli", "Broccoli"]

# i = 1
# for item in vegetables:
#     if i % 2 != 0:
#         print(item)
#     i += 1

for index, item in enumerate(vegetables):
    if index % 2 == 0:
        print(item)
