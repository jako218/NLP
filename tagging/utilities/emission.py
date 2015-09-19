#! /usr/bin/python

import sys

sys.path.insert(0, '../')
import true_global as g

def e(x, s):
    return float(g.counter.wordtag_emissions_count(s, x)) / float(g.counter.unigram_emissions_count(s))