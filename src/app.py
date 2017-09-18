#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain

from . import args

class MarkovMusic:

    def __init__(self):
        self.args = args

    def run(self):
        
        f = open("bible.txt", "r") #opens file with name of "test.txt"
        mc = MarkovChain(1)
        mc.add_string(f.read())
        markovOut = ' '.join(mc.generate_text(50))
        print markovOut