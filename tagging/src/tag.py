#! /usr/bin/python

import sys

sys.path.insert(0, '../utilities')
sys.path.insert(0, '../')
from count import Count
import parameters
import true_global
import create_dictionaries as cd

def tag(sentence):
    # Viterbi algorithm
    


if __name__ == "__main__":
    true_global.counter = Count()
    true_global.tag_dictionary = []

    counter = true_global.counter
    tag_dictionary = true_global.tag_dictionary

    try:
        input_file = file("../train/tags_dictionary.txt","r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read inputfile %s.\n" % arg)
        sys.exit(1)

    l = input_file.readline()
    while l:
        line = l.strip()
        if line:
            tag_dictionary.append(line)
        l = input_file.readline()

    dictionaries = cd.create_dictionaries()
    counter.set_training(dictionaries[0])
    counter.set_wordtags(dictionaries[1])
    counter.set_unigrams(dictionaries[2])
    counter.set_bigrams(dictionaries[3])
    counter.set_trigrams(dictionaries[4])

    word_set = []
    words = sys.argv[1].split()

    for word in words:
        if not word in counter.get_training():
            word_set.append("_RARE_")
        else:
            word_set.append(word)

    counter.set_sentence(word_set)

    tag(sys.argv[1])