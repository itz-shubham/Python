import json

# data = '{"var1": "Shubham", "var2": "Harry"}'
# # print(data)
#
# parsed = json.loads(data)
# print(parsed['var1'])

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('rice', 'cake'),
    "bad": False
}
a = json.dumps(data2)
print(a)
