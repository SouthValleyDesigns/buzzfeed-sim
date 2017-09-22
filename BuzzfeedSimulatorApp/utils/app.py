#!/usr/bin/env python

from .markov import MarkovChain
from .buzzfeedmanager import BuzzfeedManager


class BuzzfeedSimulator:
    def __init__(self):
        self.manager = BuzzfeedManager('index')
        self.training_data = []

        if not self.training_data:
            self.training_data = self.manager.read_titles()

    def train(self):
        self.training_data = self.manager.read_titles()

    def run(self):
        mc = MarkovChain(2)

        for title in self.training_data:
            mc.add_string(title)

        markovOut = ' '.join(mc.generate_text(50))

        return markovOut
