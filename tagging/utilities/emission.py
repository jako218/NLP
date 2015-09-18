#! /usr/bin/python

import sys
# import count

# sys.path.insert(0, '../src')
# from simple_tag import counter as counter

def e(x, s, counter):
    # sys.stderr.write("\nID of Counter Object: " + str(id(counter)) + "\n\n")
	
    return float(counter.wordtag_emissions_count(s, x)) / float(counter.unigram_emissions_count(s))