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
	bits = list()
	for c in line:
		bits.append(int(c))
	return bits

def listToInt(l):
	""" """
	return int("".join(map(str, l)), 2)
	
def main():
	contents = list(map(parse, slurpFile("input")))
	for l in contents:
		logging.debug(str(l))
	countOfBits = len(contents[0])
	bitCounts = list()
	for i in range(0, countOfBits):
		allBits = [ls[i] for ls in contents]
		countOfZero=0
		for b in allBits:
			if(b == 0):
				countOfZero+=1
		countOfOne=0
		for b in allBits:
			if(b == 1):
				countOfOne+=1
		bitCounts.append((countOfZero, countOfOne))
		logging.debug("Pos " + str(i) + " : (" + str(countOfZero) + ", " + str(countOfOne) + ")")
	
	gamma = list()
	epsilon = list()
	for bitCount in bitCounts:
		if(bitCount[0] < bitCount[1]):
			gamma.append(1)
			epsilon.append(0)
		else:
			gamma.append(0)
			epsilon.append(1)
	gAsInt = listToInt(gamma)
	logging.info("G: " + str(gAsInt))
	eAsInt = listToInt(epsilon)
	logging.info("E: " + str(eAsInt))
	logging.info("RATE: " + str(gAsInt * eAsInt))
	
main()
