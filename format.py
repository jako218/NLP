#! /usr/bin/python

import sys

def format_sentences(input_file):
	l = input_file.readline()
	target = open("Downloads/prelim.txt", "w")
	while l:
		line = l.strip()
		if line:
			target.write(line.replace(" ", "\n"))
			target.write("\n\n")
		l = input_file.readline()


def replace_slashes(input_file):
	l = input_file.readline()
	target = open("Downloads/output.txt", "a")
	while l:
		line = l.strip()
		if line:
			sys.stderr.write(line + "\n\n")
			target.write(line.replace("/", " "))
			target.write("\n")
		else:
			sys.stderr.write("No line found")
			target.write("\n")
		l = input_file.readline()


if __name__ == "__main__":

	try:
		input_file = file(sys.argv[1], "r")
	except IOError:
		sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
		sys.exit(1)

	format_sentences(input_file)

	try:
		input_file = file("Downloads/prelim.txt", "r")
	except IOError:
		sys.stderr.write("ERROR: Cannot read input file %s.\n" % arg)
		sys.exit(1)

	replace_slashes(input_file)