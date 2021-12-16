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
	dist = abs(f - t)
	return int(dist * (dist+1) / 2)

def func(path):
	crabPositions = parseFile(path)
	#print(crabPositions)

	maxPos = max(crabPositions)

	posCosts = list()
	for pos in range(0, maxPos):
		posCosts.append(0)
		for crab in crabPositions:
			posCosts[pos] += costToMoveFrom(crab, pos)

	#print(posCosts)
	return min(posCosts)

class TestDay7Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 168)

	def test_inputdata(self):
		self.assertEqual(func('input'), 85015836)

if __name__ == '__main__':
	unittest.main()