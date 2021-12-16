#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

from collections import deque

validOpens = ["(", "[", "{", "<"]
validCloses = [")", "]", "}", ">"]
closeToOpen = { ")" : "(", "]" : "[", "}" : "{", ">" : "<" }

closePoints = {
	")" : 3,
	"]" : 57,
	"}" : 1197,
	">" : 25137,
}

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def validate(chunk):

	stack = deque()
	for c in chunk:
		if c in validOpens:
#			print("open " + c)
			stack.append(c)
		elif c in validCloses:
			lastChar = None
			if(len(stack) > 0):
				lastChar = stack.pop()
#			print("close " + c + ", " + lastChar)
			if(closeToOpen[c] != lastChar):
				return (False, c)
		else:
#			print( "Wow I screwed up")
			return (False, None)

	return (True, None)

def func(path):
	contents = parseFile(path)

	invalidCharCounts = {
		")" : 0,
		"]" : 0,
		"}" : 0,
		">" : 0,	
	}
	for chunk in contents:
		(valid, corruptChar) = validate(chunk)
		if valid:
			# this is valid to the end but missing characters
			# print(chunk)
			pass
		else:
			#print("corrupt " + corruptChar)
			invalidCharCounts[corruptChar] += 1
			# this is the corrupt case
			pass

	score = 0
	for x in invalidCharCounts:
		count = invalidCharCounts[x]
		pointValue = closePoints[x]
		score += (count * pointValue)
	logging.debug(score)
	return score

class TestDay10Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 26397)

	def test_inputdata(self):
		self.assertEqual(func('input'), 323691)

if __name__ == '__main__':
	unittest.main()