family = {
  "child1": {
    "name": "Harry",
    "year": 2004
  },
  "child2": {
    "name": "Rohan",
    "year": 2007
  },
  "child3": {
    "name": "SkillF",
    "year": 2011
  }
}
# print(type(family))
# print(family["child1"])


# del family["child3"]
# print(family)

# children = family
# del children["child3"]  # this will delete family dictionary also
# print(family)

# children = family.copy()
# del children["child3"]  # copy of family will not affect the main family dictionary
# print(family)

# print(family.get("child2"))

# family.update({"child4": {'name': 'Shubham', 'year': 2000}})
# print(family)

print(family.items())
print(family.keys())
