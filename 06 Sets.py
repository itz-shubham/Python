fruits = {"apple", "banana", "cherry"}

# fruits = ["apple", "banana", "cherry"]
# sets_of_fruits = {"fruits"}
# print(type(sets_of_fruits))

# fruits.add("mango")
# fruits.remove("cherry")

# fruits.update(["orange", "mango", "grapes"])
# fruits.discard("cherry")
# fruits.pop()
# fruits.clear()
# print(fruits)

# print(len(fruits))
# del fruits

vegetable = {"potato", "tomato", "pea"}

# row_food = vegetable.union(fruits)
# print(row_food)

fruits.update(vegetable)
print(fruits)


