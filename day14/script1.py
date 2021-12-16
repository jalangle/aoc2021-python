#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

STEPS = 10

def parseFile(path):
	initial = ""
	insertions = dict()
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			if(initial == ""):
				initial = l
			elif(l != ""):
				(pair, insertion) = l.split(" -> ")
				insertions[pair] = insertion
	return (initial, insertions)

def insertAt(strOriginal, strToInsert, pos):
	return strOriginal[:pos] + strToInsert + strOriginal[pos:]

def func(path):
	(polymer, insertions) = parseFile(path)

	for s in range(0, STEPS):
		logging.debug("STEP " + str(s))
		for i in range(len(polymer)-2, -1, -1):
			#print("Pos: " + str(i))
			pair = polymer[i:i+2]
			#print("  Pair: " + pair)
			#print("  Before: " + polymer)
			if(pair in insertions):
				#print("  Insertion: " + insertions[pair])
				polymer = insertAt(polymer, insertions[pair], i + 1)
			#print("  After: " + polymer)
			#print("-" * 40)

	logging.debug("-" * 40)
	counts = dict()
	for c in polymer:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1

#	pp.pprint(counts)

	maxCount = 0
	minCount = 1000000000000000000000000
	for c in counts:
		if counts[c] > maxCount:
			maxCount = counts[c]
		elif counts[c] < minCount:
			minCount = counts[c]

	logging.debug(str(maxCount - minCount))

	return maxCount - minCount

class TestDay14Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 1588)

	def test_inputdata(self):
		self.assertEqual(func('input'), 2010)

if __name__ == '__main__':
	unittest.main()