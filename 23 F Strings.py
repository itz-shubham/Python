# F-String

import math

name = "Shubham"
roll = "1"

# sentence = "Hey I am %s and my roll number is %s" % (name, roll)
# print(sentence)

# sentence = "Hey I am {0} and my roll number is {1}"
# intro = sentence.format(name, roll)
# print(intro)

sentence = f"Hey I am {name} and my roll number is {roll}. cos65 = {math.cos(65)}"
print(sentence)
