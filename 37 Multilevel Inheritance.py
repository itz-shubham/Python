class Dad:
    basketball = 5


class Son(Dad):
    dance = 1
    basketball = 3

    def can_dance(self):
        return print(f"I can dance {self.dance} number of times")


class Grandson(Son):
    dance = 6

    def can_dance(self):
        return print(f"I can dance like Jackson {self.dance} number of times")


william = Dad()
james = Son()
oliver = Grandson()

print(oliver.basketball)
