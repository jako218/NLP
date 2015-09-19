#! /usr/bin/python

import sys

sys.path.insert(0, '../')
import true_global as g

def q(s1, s3, s2):
    if s3 == "*" and s2 == "*":
        return float(g.counter.unigram_count(s1)) / float(g.counter.tag_count())
    elif s3 == "*":
        return float(g.counter.bigram_count(s2, s1)) / float(g.counter.unigram_count(s2))
    elif s1 == "STOP":
        return float(g.counter.bigram_count(s3, s2))
    else:
        return float(g.counter.trigram_count(s3, s2, s1)) / float(g.counter.bigram_count(s3, s2))