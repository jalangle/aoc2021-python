#!python3
import logging
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

REPRODUCTION_RATE = 7
REPRODUCTION_MATURITY_RATE = 2

def parseFile(path):
	"""Retrieve file contents"""
	contents = None
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			contents = [int(x) for x in l.split(",")]
	return contents

def func(path, days):
	lanternfishes = parseFile(path)

	for day in range(0,days):
		newToAdd = 0
		for i in range(0, len(lanternfishes)):
			lanternfishes[i] -= 1
			if(lanternfishes[i] < 0):
				lanternfishes[i] = REPRODUCTION_RATE - 1
				lanternfishes.append(REPRODUCTION_MATURITY_RATE + REPRODUCTION_RATE -1)
#		print("After " + str(day) + " days: " + str(lanternfishes))

	return len(lanternfishes)

class TestDay6Part1(unittest.TestCase):

	def test_testdata18(self):
		self.assertEqual(func('test', 18), 26)

	def test_testdata80(self):
		self.assertEqual(func('test', 80), 5934)

	def test_inputdata(self):
		self.assertEqual(func('input',80), 391888)

if __name__ == '__main__':
	unittest.main()