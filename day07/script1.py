#!python3
import logging
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			values = l.rstrip().split(',')
			for x in values:
				contents.append(int(x))
	return contents

def costToMoveFrom(f, t):
	return abs(f - t)

def func(path):
	crabPositions = parseFile(path)
	logging.debug(crabPositions)

	maxPos = max(crabPositions)

	posCosts = list()
	for pos in range(0, maxPos):
		posCosts.append(0)
		for crab in crabPositions:
			posCosts[pos] += costToMoveFrom(crab, pos)

	logging.debug(posCosts)
	return 	min(posCosts)

class TestDay7Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 37)

	def test_inputdata(self):
		self.assertEqual(func('input'), 325528)

if __name__ == '__main__':
	unittest.main()