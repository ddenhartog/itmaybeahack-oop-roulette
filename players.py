class Player:
    def __init__(
        self,
        stake,
        rounds_to_go,
        table,
        bets=None
    ):
        self.stake = stake
        self.rounds_to_go = rounds_to_go
        self.table = table
        self.bets = bets if isinstance(bets, list) else []

    def is_playing(self):
        return True

    def place_bets(self):
        for bet in self.bets:
            print('Betting', bet)
            self.table.place_bet(bet)
            self.stake -= bet.amount

    def win(
        self,
        bet
    ):
        self.stake += bet.win_amount()

    def lose(
        self,
        bet
    ):
        #pass becuase self.stake was already reduced during self.place_bets
        pass


class Passenger57(Player): pass