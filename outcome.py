#PYTHON
import re

#PROJECT
from odds import Odds


class Outcome:
    def __init__(
        self,
        name,
        odds
    ):
        self.name = re.sub(r'[^\w -]', '', name).lower().capitalize()
        self.odds = odds

    def win_amount(
        self,
        amount
    ):
        return amount * self.odds

    def __eq__(
        self,
        other_outcome
    ):
        return self.name == other_outcome.name

    def __ne__(
        self,
        other_outcome
    ):
        return self.name != other_outcome.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return '{name} ({odds}:{to_one})'.format(
            name=self.name,
            odds=self.odds,
            to_one=Odds.TO_ONE
        )
