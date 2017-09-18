#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain
from buzzfeedmanager import BuzzfeedManager

from . import args

class BuzzfeedSimulator:

    def __init__(self):
        self.args = args

    def run(self):
<<<<<<< HEAD
        mc = MarkovChain(2)
        manager = BuzzfeedManager('lol')
        training_data = manager.read_titles()
        
        for title in training_data:
            mc.add_string(title)
        
        markovOut = ' '.join(mc.generate_text(22))
        print markovOut
=======

        f = open("bible.txt", "r") #opens file with name of "test.txt"
        mc = MarkovChain(1)
        mc.add_string(f.read())
        markovOut = ' '.join(mc.generate_text(50))
        print markovOut
>>>>>>> 67af8b4c6cf52ec928923a078d471e3ffbbab785
