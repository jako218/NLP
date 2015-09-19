#! /usr/bin/python

import sys

sys.path.insert(0, '../utilities')
from count import Count
import emission
import create_dictionaries as cd


def tag(sentence):
    result = ""
    words = sentence.split()
    for word in words:
        result = result + word + "/" + tag_word(word) + " "

    sys.stderr.write(result)


def tag_word(word):

    if not word in counter.get_training():
        word = "_RARE_"

    max_e = 0
    max_tag = "NA"
    for tag in tag_dictionary:
        e = emission.e(word, tag, counter)
        if e > max_e:
            max_e = e
            max_tag = tag

    return max_tag



if __name__ == "__main__":
    global counter
    global tag_dictionary

    counter = Count()
    tag_dictionary = []

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

    tag(sys.argv[1])



