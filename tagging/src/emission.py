#! /usr/bin/python

import sys
import count

def e(x, s):
	return float(count.bigram_emissions_count(s, x)) / float(count.unigram_emissions_count(s))

if __name__ == "__main__":
	sys.stderr.write(str(e("the", "at-tl")))