#! /usr/bin/python

import sys

def create_rare_tag(tags_file, counts_file):
    rare_words = []
    c = counts_file.readline()
    while c:
        c_line = c.strip()
        if c_line:
            c_parts = c_line.split()
            if c_parts[1] == "WORDTAG" and int(c_parts[0]) < 5:
                rare_words.append(c_parts[3])
        c = counts_file.readline()

    target = open("./rare_tags.txt", "w")
    t = tags_file.readline()
    while t:
        t_line = t.strip()
        if t_line:
            t_parts = t_line.split()
            if t_parts[0] in rare_words:
                target.write("_RARE_ " + t_parts[1] + "\n")
            else:
                target.write(t_line + "\n")
        else:
            target.write("\n")
        t = tags_file.readline()



if __name__ == "__main__":

    try:
        tags_file = file("tagging/train/tags.txt", "r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
        sys.exit(1)

    try:
        counts_file = file("tagging/train/tags.counts", "r")
    except IOError:
        sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
        sys.exit(1)

    create_rare_tag(tags_file, counts_file)