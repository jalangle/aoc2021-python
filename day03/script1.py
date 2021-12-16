#!python3
import logging
import unittest

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
	
def func(path):
	contents = list(map(parse, slurpFile(path)))
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
	logging.debug("G: " + str(gAsInt))
	eAsInt = listToInt(epsilon)
	logging.debug("E: " + str(eAsInt))
	logging.debug("RATE: " + str(gAsInt * eAsInt))
	return gAsInt * eAsInt
	
class TestDay3Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 198)

	def test_inputdata(self):
		self.assertEqual(func('input'), 2724524)

if __name__ == '__main__':
	unittest.main()