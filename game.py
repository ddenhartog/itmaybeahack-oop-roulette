#PROJECT
from bin import BinBuilder


class Game:
    def __init__(
        self,
        wheel,
        table
    ):
        self.wheel = wheel
        self.table = table
        BinBuilder(self.wheel).build_bins()

    def play_round(
        self,
        player
    ):
        print('Placing bets...')
        #one print() in player.place_bets()
        player.place_bets()
        print('Bets placed.')
        print('Spinning wheel...')
        number, bin = self.wheel.spin()
        number = str(number) if number < 37 else '00'
        print('Wheel stopped spinning on', number)
        print('The wheel stopping on', number, 'means any of the following bets are winners:', bin)
        print('Checking bets...')
        for bet in self.table:
            print('Checking', bet)
            if bet.outcome in bin.outcomes:
                print('Congratulations! You won', '${}'.format(bet.win_amount()))
                player.win(bet)
            else:
                print('Sorry, your bet wasn\'t a winner. Better luck next time!')
                player.lose(bet)
        print('Clearing table of bets...')
        self.table.clear_bets()


data = FinancialStatementDataModel.objects.raw('SELECT max(date_reported) from {table_name} WHERE date_reported < %s'.format(table_name=FinancialStatementDataModel._meta.db_table), [])