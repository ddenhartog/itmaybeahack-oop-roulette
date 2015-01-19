#PROJECT
from outcome import Outcome
from odds import Odds


class Bin:
    def __init__(
        self,
        *outcomes
    ):
        self.outcomes = set([outcome for outcome in outcomes])

    def add_outcome(
        self,
        outcome
    ):
        self.outcomes.add(outcome)

    def __str__(self):
        return ', '.join([str(outcome) for outcome in self.outcomes])


class BinBuilder:
    def __init__(
        self,
        wheel
    ):
        self.wheel = wheel

    def build_bins(self):
        self.straight_bets()
        self.split_bets()
        self.street_bets()
        self.corner_bets()
        self.five_bet()
        self.line_bets()
        self.dozen_bets()
        self.column_bets()
        self.even_money_bets()

    def straight_bets(self):
        outcomes = [
            Outcome(str(i), Odds.STRAIGHT_BET)
            for i in range(37)
        ] + [Outcome('00', Odds.STRAIGHT_BET)]
        for i, outcome in enumerate(outcomes):
            self.wheel.add_outcome(i, outcome)

    def split_bets(self):
        for row in range(12):
            for direction in [1, 2]:
                n = 3 * row + direction
                bins = [n, n + 1]
                outcome = Outcome(
                    'split {}'.format('-'.join([str(i) for i in bins])),
                    Odds.SPLIT_BET
                )
                for bin in bins:
                    self.wheel.add_outcome(bin, outcome)

        for n in range(1, 34):
            bins = [n, n + 3]
            outcome = Outcome(
                'split {}'.format('-'.join([str(i) for i in bins])),
                Odds.SPLIT_BET
            )
            for bin in bins:
                self.wheel.add_outcome(bin, outcome)

    def street_bets(self):
        for row in range(12):
            n = 3 * row + 1
            bins = [n, n + 1, n + 2]
            outcome = Outcome(
                'street {}-{}'.format(bins[0], bins[-1]),
                Odds.STREET_BET
            )
            for bin in bins:
                self.wheel.add_outcome(bin, outcome)

    def corner_bets(self):
        for col in [1, 2]:
            for row in range(11):
                n = 3 * row + col
                bins = [n + i for i in [0, 1, 3, 4]]
                outcome = Outcome(
                    'corner {}'.format('-'.join([str(i) for i in bins])),
                    Odds.CORNER_BET
                )
                for bin in bins:
                    self.wheel.add_outcome(bin, outcome)

    def five_bet(self):
        outcome = Outcome(
            'five bet 00-0-1-2-3',
            Odds.FIVE_BET
        )
        for bin in [0, 1, 2, 3, 37]:
            self.wheel.add_outcome(bin, outcome)

    def line_bets(self):
        for row in range(11):
            n = 3 * row + 1
            bins = [n + i for i in range(6)]
            outcome = Outcome(
                'line {}-{}'.format(bins[0], bins[-1]),
                Odds.LINE_BET
            )
            for bin in bins:
                self.wheel.add_outcome(bin, outcome)

    def dozen_bets(self):
        #https://pypi.python.org/pypi/inflect/0.2.4
        dozen_map = {
            1: '1st',
            2: '2nd',
            3: '3rd'
        }
        for d in range(3):
            outcome = Outcome(
                '{} 12'.format(dozen_map[d + 1]),
                Odds.DOZEN_BET
            )
            for m in range(12):
                self.wheel.add_outcome(12 * d + m + 1, outcome)

    def column_bets(self):
        for c in range(3):
            outcome = Outcome(
                'column {}'.format(c + 1),
                Odds.COLUMN_BET
            )
            for r in range(12):
                self.wheel.add_outcome(3 * r + c + 1, outcome)

    def even_money_bets(self):
        for bin in range(1, 37):
            if 1 <= bin < 19:
                name = '1 to 18'  #low
            else:
                name = '19 to 36'  #high
            self.wheel.add_outcome(
                bin,
                Outcome(name, Odds.EVEN_MONEY_BET)
            )

            if bin % 2:
                name = 'odd'
            else:
                name = 'even'
            self.wheel.add_outcome(
                bin,
                Outcome(name, Odds.EVEN_MONEY_BET)
            )

            if bin in (
                [1, 3, 5, 7, 9] +
                [12, 14, 16, 18] +
                [19, 21, 23, 25, 27] +
                [30, 32, 34, 36]
            ):
                name = 'red'
            else:
                name = 'black'
            self.wheel.add_outcome(
                bin,
                Outcome(name, Odds.EVEN_MONEY_BET)
            )
