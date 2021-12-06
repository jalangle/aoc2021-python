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

	horiz = 0
	depth = 0
	aim = 0

	for c in contents:
		if(c[0] == "forward"):
			horiz += c[1]
			depth += (aim * c[1])
		elif(c[0] == "down"):
			aim += c[1]
		elif(c[0] == "up"):
			aim -= c[1]

	print("Horizontal Postition: " + str(horiz))
	print("Depth: " + str(depth))
	print("H*D: " + str(horiz * depth))

main()
