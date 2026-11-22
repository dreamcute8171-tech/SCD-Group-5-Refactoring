
class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yatzy(dice):
        counts = [0] * 6

        for die in dice:
            counts[die - 1] += 1

        for i in range(6):
            if counts[i] == 5:
                return 50

        return 0

    @staticmethod
    def _sum_matching_dice(dice, number):
        total = 0

        for die in dice:
            if die == number:
                total += number

        return total

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        return Yatzy._sum_matching_dice(
            [d1, d2, d3, d4, d5], 1
        )

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        return Yatzy._sum_matching_dice(
            [d1, d2, d3, d4, d5], 2
        )

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        return Yatzy._sum_matching_dice(
            [d1, d2, d3, d4, d5], 3
        )

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        return Yatzy._sum_matching_dice(self.dice, 4)

    def fives(self):
        return Yatzy._sum_matching_dice(self.dice, 5)

    def sixes(self):
        return Yatzy._sum_matching_dice(self.dice, 6)

    @staticmethod
    def _count_dice(dice):
        counts = [0] * 6

        for die in dice:
            counts[die - 1] += 1

        return counts

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = Yatzy._count_dice(
            [d1, d2, d3, d4, d5]
        )

        for i in range(5, -1, -1):
            if counts[i] >= 2:
                return (i + 1) * 2

        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = Yatzy._count_dice(
            [d1, d2, d3, d4, d5]
        )

        pairs = 0
        score = 0

        for i in range(5, -1, -1):
            if counts[i] >= 2:
                pairs += 1
                score += (i + 1) * 2

        if pairs == 2:
            return score

        return 0

    @staticmethod
    def _score_n_of_a_kind(dice, n):
        counts = Yatzy._count_dice(dice)

        for i in range(6):
            if counts[i] >= n:
                return (i + 1) * n

        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        return Yatzy._score_n_of_a_kind(
            [d1, d2, d3, d4, d5], 3
        )

    @staticmethod
    def four_of_a_kind(d1, d2, d3, d4, d5):
        return Yatzy._score_n_of_a_kind(
            [d1, d2, d3, d4, d5], 4
        )

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = Yatzy._count_dice(
            [d1, d2, d3, d4, d5]
        )

        if all(tallies[i] == 1 for i in range(5)):
            return 15

        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = Yatzy._count_dice(
            [d1, d2, d3, d4, d5]
        )

        if all(tallies[i] == 1 for i in range(1, 6)):
            return 20

        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        dice = [d1, d2, d3, d4, d5]
        counts = Yatzy._count_dice(dice)

        pair = 0
        triple = 0

        for i in range(6):
            if counts[i] == 2:
                pair = i + 1
            elif counts[i] == 3:
                triple = i + 1

        if pair and triple:
            return pair * 2 + triple * 3

        return 0
