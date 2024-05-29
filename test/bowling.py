# class Game:
#     def roll(self, pins):
#         pass
#
#     def score(self):
#         return 0

class Game:
    def __init__(self):
        self.rolls = [0] * 21
        self.roll_index = 0

    def roll(self, pins):
        self.rolls[self.roll_index] = pins
        self.roll_index += 1

    def score(self):
        result = 0
        for roll in self.rolls:
            result += roll
        return result
