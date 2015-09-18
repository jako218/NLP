#! /usr/bin/python

import sys

def create_dictionaries():
    training = set()
    wordtags = {}
    unigrams = {}
    bigrams = {}
    trigrams = {}

    try:
        input_file = file("../train/rare_tags.counts", "r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
        sys.exit(1)

    l = input_file.readline()
    while l:
        line = l.strip()
        if line:
            parts = line.split()
            if parts[1] == "WORDTAG":
                key = parts[3] + " " + parts[2]
                wordtags[key] = parts[0]
                if not parts[3] in training:
                    training.add(parts[3])
            elif parts[1] == "1-GRAM":
                unigrams[parts[2]] = parts[0]
            elif parts[1] == "2-GRAM":
                key = parts[2] + " " + parts[3]
                bigrams[key] = parts[0]
            elif parts[1] == "3-GRAM":
                key = parts[2] + " " + parts[3] + " " + parts[4]
                trigrams[key] = parts[0]
            else:
                sys.stderr.write("Invalid rare_tags input line")
                sys.exit(1)

        l = input_file.readline()
    
    return training, wordtags, unigrams, bigrams, trigrams
