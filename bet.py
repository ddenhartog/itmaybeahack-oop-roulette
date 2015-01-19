class Bet:
    def __init__(
        self,
        amount,
        outcome
    ):
        self.amount = amount
        self.outcome = outcome

    def win_amount(self):
        return self.outcome.win_amount(self.amount)

    def lose_amount(self):
        return self.amount

    def __str__(self):
        return '${amount} on {outcome}'.format(
            amount=self.amount,
            outcome=self.outcome
        )
