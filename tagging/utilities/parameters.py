#! /usr/bin/python

import sys

sys.path.insert(0, '../')
import true_global as g

def e(x, s):
    return float(g.counter.wordtag_count(s, x)) / float(g.counter.unigram_count(s))

def q(s1, s3, s2):
    if s3 == "*" and s2 == "*":
        return float(g.counter.unigram_count(s1)) / float(g.counter.tag_count())
    elif s3 == "*":
        return float(g.counter.bigram_count(s2, s1)) / float(g.counter.unigram_count(s2))
    elif s1 == "STOP":
        return float(g.counter.bigram_count(s3, s2))
    else:
        return float(g.counter.trigram_count(s3, s2, s1)) / float(g.counter.bigram_count(s3, s2))

def r(words, tags):
    value = 1
    for i in range(2, len(tags)):
        value = value * q(tags[i], tags[i-2], tags[i-1]) * e(words[i], tags[i])

    return value

def pi(k, u, v):
    if k == 0 and u == "*" and v == "*":
        return 1

    max(pi(k-1, w, u) * q(v, w, u) * e(g.counter.get_sentence[k], v))
