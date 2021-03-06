#! /usr/bin/python

import sys

class Count(object):
	def __init__(self):
		self._sentence = []
		self._training = set()
		self._wordtags = {}
		self._unigrams = {}
		self._bigrams = {}
		self._trigrams = {}

	def get_sentence(self):
		return self._sentence

	def get_training(self):
		return self._training

	def get_wordtags(self):
		return self._wordtags

	def get_unigrams(self):
		return self._unigrams

	def get_bigrams(self):
		return self._bigrams

	def get_trigrams(self):
		return self._trigrams

	def set_sentence(self, sentence):
		self._sentence = sentence

	def set_training(self, training):
		self._training = training

	def set_wordtags(self, wordtags):
		self._wordtags = wordtags

	def set_unigrams(self, unigrams):
		self._unigrams = unigrams

	def set_bigrams(self, bigrams):
		self._bigrams = bigrams

	def set_trigrams(self, trigrams):
		self._trigrams = trigrams


	def wordtag_count(self, s, x):
		key = x + " " + s
		if key in self._wordtags:
			return self._wordtags[key]

		return 0

	def tag_count(self):
		count = 0
		for key in self._unigrams:
			count += int(self._unigrams[key])
		
		return count

	def unigram_count(self, s):
		if s in self._unigrams:
			return self._unigrams[s]

		return 0
		
	def bigram_count(self, s1, s2):
		key = s1 + " " + s2
		sys.stderr.write(key + "\n")
		if key in self._bigrams:
			return self._bigrams[key]

		return 0

	def trigram_count(self, s1, s2, s3):
		key = s1 + " " + s2 + " " + s3
		if key in self._trigrams:
			return self._trigrams[key]

		return 0