#!python3
import logging
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

REPRODUCTION_RATE = 7
REPRODUCTION_MATURITY_RATE = 2

def newFish(interval, count):
	return { "count" : count, "interval" : interval }

def parseFile(path):
	"""Retrieve file contents"""
	contents = None
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			intervals = [int(x) for x in l.split(",")]
			contents = [newFish(x, 1) for x in intervals]
	return contents

def func(path, days):
	lanternfishes = parseFile(path)

	for day in range(0,days):
		numberToAdd = 0
		for i in range(0, len(lanternfishes)):
			lanternfishes[i]["interval"] -= 1
			if(lanternfishes[i]["interval"] < 0):
				lanternfishes[i]["interval"] = REPRODUCTION_RATE - 1
				numberToAdd += lanternfishes[i]["count"]

		if(numberToAdd > 0):
			lanternfishes.append(newFish(REPRODUCTION_MATURITY_RATE + REPRODUCTION_RATE - 1, count=numberToAdd))

	count = 0
	for f in lanternfishes:
		count += f["count"]

	return count

class TestDay6Part1(unittest.TestCase):

	def test_testdata18(self):
		self.assertEqual(func('test', 18), 26)

	def test_testdata80(self):
		self.assertEqual(func('test', 80), 5934)

	def test_inputdata80(self):
		self.assertEqual(func('input',80), 391888)

	def test_inputdata256(self):
		self.assertEqual(func('input',256), 1754597645339)

if __name__ == '__main__':
	unittest.main()