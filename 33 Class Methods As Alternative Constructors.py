# text = "Python tutorial for absolute beginners."
# spited_text = text.split()
# print(spited_text)

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


date1 = Date.from_dash("2008-12-5")
print(date1.year)
# Output: 2008
