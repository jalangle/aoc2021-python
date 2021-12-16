#!python3
import logging
import unittest

from copy import deepcopy

logging.basicConfig(filemode='w', level=logging.INFO)

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

def countTheBits(i, allBits):
	countOfZero=0
	for b in allBits:
		if(b == 0):
			countOfZero+=1
	countOfOne=0
	for b in allBits:
		if(b == 1):
			countOfOne+=1

	return(countOfZero, countOfOne)

def mostCommonBit(i, allBits):
	(countOfZero, countOfOne) = countTheBits(i, allBits)
	if(countOfZero > countOfOne):
		return 0
	return 1

def get_oxygen_rating(countOfBits, o2rating):
	for i in range(0, countOfBits):
		if(len(o2rating) == 1):
			break
		allBits = [ls[i] for ls in o2rating]
		mostCommon = mostCommonBit(i, allBits)
		o2rating = [x for x in o2rating if x[i] == mostCommon]

	logging.debug(o2rating[0])
	return listToInt(o2rating[0])

def leastCommonBit(i, allBits):
	(countOfZero, countOfOne) = countTheBits(i, allBits)
	if(countOfZero > countOfOne):
		return 1
	return 0

def get_co2_rating(countOfBits, co2rating):

	for i in range(0, countOfBits):
		if(len(co2rating) == 1):
			break

		allBits = [ls[i] for ls in co2rating]
		leastCommon = leastCommonBit(i, allBits)

		logging.debug("------------------")
		logging.debug("Elems: " + str(len(co2rating)) + "-" + str(co2rating))
		logging.debug("LC: " + str(leastCommon))
		logging.debug("I: " + str(i))
		co2rating = [x for x in co2rating if x[i] == leastCommon]
		logging.debug("Elems: " + str(len(co2rating)) + "-" + str(co2rating))
		if(len(co2rating) == 0):
			return
	
	logging.debug("After: " + str(co2rating))

	logging.debug(co2rating[0])
	return listToInt(co2rating[0])

def func(path):
	contents = list(map(parse, slurpFile(path)))
	countOfBits = len(contents[0])

	o2 = get_oxygen_rating(countOfBits, deepcopy(contents))
	co2 = get_co2_rating(countOfBits, deepcopy(contents))	
	logging.debug("Life Support Rating: " + str(o2 * co2))
	return o2 * co2

class TestDay3Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 230)

	def test_inputdata(self):
		self.assertEqual(func('input'), 2775870)

if __name__ == '__main__':
	unittest.main()