#! /usr/bin/python

import sys

sys.path.insert(0, '../')
import true_global as g

def e(x, s):
    return float(g.counter.wordtag_count(s, x)) / float(g.counter.unigram_count(s))