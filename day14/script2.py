#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

STEPS = 40

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

def func(path):
	(polymer, insertions) = parseFile(path)

	segmentCounts = dict.fromkeys(insertions, 0)

	for i in range(0,len(polymer)-1):
		segment = polymer[i:i+2]
		segmentCounts[segment] += 1

	for step in range(0, STEPS):
		counts = dict.fromkeys(segmentCounts, 0)
		for segment in segmentCounts:
			insertion = insertions[segment]
			counts[segment[0] + insertion] += segmentCounts[segment]
			counts[insertion + segment[1]] += segmentCounts[segment]
		segmentCounts = counts

	letterCounts = dict()
	for segment in segmentCounts:
		for c in segment:
			if c in letterCounts:
				letterCounts[c] += segmentCounts[segment]
			else:
				letterCounts[c] = segmentCounts[segment]

	for letter in letterCounts:
		if letterCounts[letter] % 2 == 1:
			letterCounts[letter] = ( letterCounts[letter] // 2 ) + 1
		else:
			letterCounts[letter] = ( letterCounts[letter] // 2 )

	maximum = max(x for x in letterCounts.values())
	minimum = min(x for x in letterCounts.values())

	logging.debug(str(maximum - minimum))
	return maximum - minimum

class TestDay14Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 2188189693529)

	def test_inputdata(self):
		self.assertEqual(func('input'), 2437698971143)

if __name__ == '__main__':
	unittest.main()