import random


class Company(object):
    def __init__(self, money):
        #self.money = random.randrange(10)
        self.money = money

    def __eq__(self, other):
        return self.money == other.money

    def __gt__(self, other):
        return self.money > other.money

    def __ge__(self, other):
        return self.money >= other.money

    def __lt__(self, other):
        return self.money < other.money

    def __le__(self, other):
        return self.money <= other.money


    # def __cmp__(self, other):
    #     if self.money < other.money:
    #         return -1
    #     elif self.money == other.money:
    #         return 0
    #     else:
    #         return 1
