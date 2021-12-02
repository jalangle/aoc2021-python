#!python3
from itertools import islice
import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

WINDOWSIZE = 3

def slurpFile(path):
	"""Retrieve file contents"""
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def parse(line):
	""" """
	(command, value) = line.split(' ')
	return(command, int(value))

def main():
	contents = list(map(parse, slurpFile("input")))


main()
