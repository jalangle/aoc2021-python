#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

from collections import deque

validOpens = ["(", "[", "{", "<"]
validCloses = [")", "]", "}", ">"]
openToClose = { 
	"(" : ")",
	"[": "]",
	"{" : "}",
	"<" : ">"
}
closeToOpen = {
	")" : "(",
	"]" : "[",
	"}" : "{",
	">" : "<"
}
closePoints = {
	")" : 1,
	"]" : 2,
	"}" : 3,
	">" : 4,
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

	completion = ""
	while(len(stack) > 0):
		completion += openToClose[stack.pop()]

	return (True, completion)

def scoreCompletion(completion):
	s = 0
	for c in completion:
		s *= 5
		s += closePoints[c]

	return s;

def func(path):
	contents = parseFile(path)

	invalidCharCounts = {
		")" : 0,
		"]" : 0,
		"}" : 0,
		">" : 0,	
	}
	scores = list()

	for chunk in contents:
		(valid, extra) = validate(chunk)
		if valid:
			# this is valid to the end but missing characters
#			print(chunk + "    " + extra)
			s = scoreCompletion(extra)
#			print(s)
			scores.append(s)
			pass
		else:
			#print("corrupt " + extra)
			invalidCharCounts[extra] += 1
			# this is the corrupt case
			pass

	scores.sort()
	#pp.pprint(scores)
	middleIndex = int((len(scores)) / 2)
	#pp.pprint(middleIndex)
	#pp.pprint(scores[middleIndex])
	return scores[middleIndex]

class TestDay10Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 288957)

	def test_inputdata(self):
		self.assertEqual(func('input'), 2858785164)

if __name__ == '__main__':
	unittest.main()