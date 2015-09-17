#! /usr/bin/python

def get_tags(counts_file):
    tags = []
    l = counts_file.readline()
    while l:
        line = l.strip()
        if line:
            parts = line.split()
            if parts[2] not in tags:
                tags.append(parts[2])
        l =counts_file.readline()
    target = open("../train/tags_dictionary.txt", "w")
    for tag in tags:
        target.write(tag + "\n")