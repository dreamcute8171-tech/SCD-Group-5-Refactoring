
class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return Yatzy._sum_dice([d1, d2, d3, d4, d5])

    @staticmethod
    def _sum_dice(dice):
        total = 0
        for die in dice:
            total += die
        return total

    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)

        for die in dice:
            counts[die - 1] += 1

        for i in range(len(counts)):
            if counts[i] == 5:
                return 50

        return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        total = 0
        if d1 == 1:
            total += 1
        if d2 == 1:
            total += 1
        if d3 == 1:
            total += 1
        if d4 == 1:
            total += 1
        if d5 == 1:
            total += 1
        return total

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        total = 0
        if d1 == 2:
            total += 2
        if d2 == 2:
            total += 2
        if d3 == 2:
            total += 2
        if d4 == 2:
            total += 2
        if d5 == 2:
            total += 2
        return total

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        total = 0
        if d1 == 3:
            total += 3
        if d2 == 3:
            total += 3
        if d3 == 3:
            total += 3
        if d4 == 3:
            total += 3
        if d5 == 3:
            total += 3
        return total

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        total = 0
        for at in range(5):
            if self.dice[at] == 4:
                total += 4
        return total

    def fives(self):
        total = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 5:
                total += 5
        return total

    def sixes(self):
        total = 0
        for at in range(len(self.dice)):
            if self.dice[at] == 6:
                total += 6
        return total

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1

        for at in range(6):
            if counts[6 - at - 1] == 2:
                return (6 - at) * 2

        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1

        n = 0
        score = 0

        for i in range(6):
            if counts[6 - i - 1] >= 2:
                n += 1
                score += (6 - i)

        if n == 2:
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4

        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] >= 3:
                return (i + 1) * 3

        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15

        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1 and
            tallies[5] == 1):
            return 20

        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        has_pair = False
        pair_value = 0
        has_three = False
        three_value = 0

        for i in range(6):
            if tallies[i] == 2:
                has_pair = True
                pair_value = i + 1

        for i in range(6):
            if tallies[i] == 3:
                has_three = True
                three_value = i + 1

        if has_pair and has_three:
            return pair_value * 2 + three_value * 3
        else:
            return 0
