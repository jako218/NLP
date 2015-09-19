#! /usr/bin/python

import sys

sys.path.insert(0, '../src')
from simple_tag import *

def e(x, s, counter):
    return float(counter.wordtag_emissions_count(s, x)) / float(counter.unigram_emissions_count(s))