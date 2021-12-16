#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

from collections import deque

class Edge:
	def __init__(self):
		self.begin = None
		self.end = None

	def __str__(self):
		return "(" + self.begin + "," + self.end + ")"

	def __repr__(self):
		return str(self)

	def hasEndpoint(self, pt):
		return self.begin == pt or self.end == pt

	def isStart(self):
		return self.begin == "start"

	def isEnd(self):
		return self.begin == "end"

	def isNamedLocation(self):
		return isStart() or isEnd()


def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			(begin, end) = l.rstrip().split('-')
			p = Edge()
			p.begin = begin
			p.end = end
			contents.append(p)
	return contents

def isLargeCave(cave):	
	logging.debug(cave + " != " + cave.lower())
	return cave != cave.lower()

def canVisit(cave, stack):
	if not cave in stack:
		return True
	return isLargeCave(cave)

def getVisitable(tree, cave, stack):
	visitable = list()
	connectedEdges = [x for x in tree if x.hasEndpoint(cave)]
	logging.debug(cave + " is connected to " + str(connectedEdges))
	for edge in connectedEdges:
		nextCave = edge.end if cave == edge.begin else edge.begin
		logging.debug("Next: " + nextCave)
		if cave == nextCave:
			continue
		if canVisit(nextCave, stack):
			visitable.append(nextCave)

	logging.debug(cave + " can visit " + str(visitable))
	return visitable

def visit(tree, cave, stack, paths):
	if(len(stack) > 100):
		return

	stack.append(cave)
	logging.debug("\t" * len(stack) + cave)
	if(cave == "end"):
		paths.append(",".join(stack))
		stack.pop()
		return

	nextCaves = getVisitable(tree, cave, stack)
	for cave in nextCaves:
		visit(tree, cave, stack, paths)

	stack.pop()

	return paths

def func(path):
	cavePaths = parseFile(path)

	paths = visit(cavePaths, "start", deque(), list())
#	pp.pprint(paths)
	logging.debug(len(paths))
	return len(paths)

class TestDay12Part1(unittest.TestCase):

	def test_testdata1(self):
		self.assertEqual(func('test1'), 10)

	def test_testdata2(self):
		self.assertEqual(func('test2'), 19)

	def test_testdata3(self):
		self.assertEqual(func('test3'), 226)

	def test_inputdata(self):
		self.assertEqual(func('input'), 4691)

if __name__ == '__main__':
	unittest.main()