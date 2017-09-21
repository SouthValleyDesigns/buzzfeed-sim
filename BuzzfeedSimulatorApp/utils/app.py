#!/usr/bin/env python

from .markov import MarkovChain
from .buzzfeedmanager import BuzzfeedManager


class BuzzfeedSimulator:
    def run(self):
        mc = MarkovChain(1)
        manager = BuzzfeedManager('lol')
        training_data = manager.read_titles()

        for title in training_data:
            mc.add_string(title)

        markovOut = ' '.join(mc.generate_text(30))

        return markovOut
