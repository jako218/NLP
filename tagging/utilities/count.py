#! /usr/bin/python

import sys

def unigram_emissions_count(s):
	input_file = get_file("../train/tags.counts")
	l = input_file.readline()
	while l:
		line = l.strip()
		if line:
			parts = line.split()
			if parts[1] == "1-GRAM" and parts[2] == s:
				return parts[0]
		l = input_file.readline()

	return 0
	

def bigram_emissions_count(s, x):
	input_file = get_file("../train/tags.counts")
	l = input_file.readline()
	while l:
		line = l.strip()
		if line:
			parts = line.split()
			if parts[1] == "WORDTAG" and parts[2] == s and parts[3] == x:
				return parts[0]
		l = input_file.readline()

	return 0


def get_file(filename):
	try:
		input_file = file(filename, "r")
	except IOError:
		sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
		sys.exit(1)

	return input_file


if __name__ == "__main__":
	bigram_emissions_count("at-tl", "the")
	unigram_emissions_count("at-tl")