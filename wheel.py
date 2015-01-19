#PYTHON
from random import choice

#PROJECT
from bin import Bin


class Wheel:
    def __init__(self):
        self.bins = tuple(Bin() for i in range(38))
        self.outcomes = {}

    def add_outcome(
        self,
        bin_index,
        outcome
    ):
        self.bins[bin_index].add_outcome(outcome)
        name = str(outcome).split(' (')[0]
        self.outcomes.update({name: outcome})

    def spin(self):
        #return choice(self.bins)
        index = choice(range(38))
        return index, self.bins[index]

    def get_bin(
        self,
        bin_index
    ):
        return self.bins[bin_index]

    def get_outcome(
        self,
        name
    ):
        return self.outcomes.get(name, None)
