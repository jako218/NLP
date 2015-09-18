#! /usr/bin/python

import sys

sys.path.insert(0, '../utilities')
import emission


tag_dictionary = []

def tag(sentence):
    result = ""
    words = sentence.split()
    for word in words:
        result = result + word + "/" + tag_word(word) + " "

    sys.stderr.write(result)


def tag_word(word):
    global tag_dictionary

    max_e = 0
    max_tag = "NA"
    for tag in tag_dictionary:
        e = emission.e(word, tag)
        if e > max_e:
            max_e = e
            max_tag = tag

    return max_tag



if __name__ == "__main__":
    global tag_dictionary

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

    tag(sys.argv[1])

