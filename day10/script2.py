#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
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

def main():
	contents = parseFile("input")

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
	pp.pprint(scores)
	middleIndex = int((len(scores)) / 2)
	pp.pprint(middleIndex)
	pp.pprint(scores[middleIndex])

main()