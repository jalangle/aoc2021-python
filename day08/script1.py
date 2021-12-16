#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

pp = pprint.PrettyPrinter(indent=4)

# Normally....
# 0: abcefg = 6
# 1: cf = 2
# 2: acdeg = 5
# 3: acdfg = 5
# 4: bcdf = 4
# 5: abdfg = 5
# 6: abdefg = 6
# 7: acf = 3
# 8: abcdefg = 7
# 9: abdcfg = 6

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			(inputs, outputs) = l.rstrip().split('|')
			item = dict()
			item["inputs"] = inputs.lstrip().split(' ')
			item["outputs"] = outputs.lstrip().split(' ')

			contents.append(item)
	return contents

def func(path):
	contents = parseFile(path)
#	pp.pprint(contents)
	digitCounts = list()
	for i in range(0,10):
		digitCounts.append(0)

	for row in contents:
		for digit in row["outputs"]:
			if(len(digit) == 2):
				digitCounts[1] += 1
			elif(len(digit) == 4):
				digitCounts[4] += 1
			elif(len(digit) == 3):
				digitCounts[7] += 1
			elif(len(digit) == 7):
				digitCounts[8] += 1

	return sum(digitCounts)

class TestDay8Part1(unittest.TestCase):

	def test_testdata1(self):
		self.assertEqual(func('test1'), 0)

	def test_testdata(self):
		self.assertEqual(func('test2'), 26)

	def test_inputdata(self):
		self.assertEqual(func('input'), 456)

if __name__ == '__main__':
	unittest.main()