#PROJECT
from exceptions import InvalidBet


class Table:
    def __init__(
        self,
        limit,
        bets=None
    ):
        self.limit = limit
        self.bets = bets if isinstance(bets, list) else []

    def is_valid(
        self,
        bet
    ):
        return True if sum([bet.amount] + [_bet.amount for _bet in self.bets]) <= self.limit else False

    def place_bet(
        self,
        bet
    ):
        if self.is_valid(bet):
            self.bets.append(bet)
        else:
            raise InvalidBet('The sum of all bets, including this bet, exceeds the table limit')

    def clear_bets(self):
        self.bets = []

    def __iter__(self):
        #we need to be able remove Bets from the table.
        #consequently, we have to update the list,
        #which requires that we create a copy of the list.
        #i.e.: self.bets[:].
        return iter(self.bets[:])

    def __str__(self):
        return str(self.bets)
