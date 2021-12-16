#!python3
import logging
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

def strToPoint(str):
	(x,y) = str.split(",")
	return {"x" : int(x), "y": int(y)}

def parseFile(path):
	"""Retrieve file contents"""
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			(begin,end) = l.split(" -> ")
			begin = strToPoint(begin)
			end = strToPoint(end)
			contents.append({"begin": begin, "end": end})

	return contents

MAX_WIDTH = 1000
MAX_HEIGHT = 1000

def isVertical(a, b):
	return a["x"] == b["x"]

def isHorizontal(a, b):
	return a["y"] == b["y"]

def printGrid(grid):
	logging.debug(grid)

def incrementGrid(grid, x, y):
	index = x * MAX_HEIGHT + y
	if(index in grid):
		grid[index] += 1
	else:
		grid[index] = 1

def addDelta(pt, delta):
	return { "x" : (pt["x"] + delta["x"]), "y" : (pt["y"] + delta["y"]) }

def func(path):
	contents = parseFile(path)

	grid = dict()

	for line in contents:
		begin = line["begin"]
		end = line["end"]

		if(isVertical(begin, end)):
#			logging.debug("V: " + str(line))
			low = min(begin["y"], end["y"])
			high = max(begin["y"], end["y"])
			for j in range(low, high+1):
				incrementGrid(grid, begin["x"], j)
		elif(isHorizontal(begin, end)):
#			logging.debug("H: " + str(line))
			low = min(begin["x"], end["x"])
			high = max(begin["x"], end["x"])
			for j in range(low, high+1):
				incrementGrid(grid, j, begin["y"])
		else:
#			logging.debug("D: " + str(line))
			if begin["x"] < end["x"]:
				xDelta = 1
			else:
				xDelta = -1

			if begin["y"] < end["y"]:
				yDelta = 1
			else:
				yDelta = -1

			delta = { "x" : xDelta, "y" : yDelta }
			logging.debug(delta)

			start = begin
			while(start != end):
				incrementGrid(grid, start["x"], start["y"])
				start = addDelta(start, delta)
			incrementGrid(grid, end["x"], end["y"])


	count = 0;
	for k in grid:
		if grid[k] > 1:
			count += 1

	return count

class TestDay5Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 12)

	def test_inputdata(self):
		self.assertEqual(func('input'), 22116)

if __name__ == '__main__':
	unittest.main()