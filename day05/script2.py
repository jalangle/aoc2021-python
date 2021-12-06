#!python3

from collections import ChainMap
import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

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
	print(grid)

def incrementGrid(grid, x, y):
	index = x * MAX_HEIGHT + y
	if(index in grid):
		grid[index] += 1
	else:
		grid[index] = 1

def addDelta(pt, delta):
	return { "x" : (pt["x"] + delta["x"]), "y" : (pt["y"] + delta["y"]) }

def main():
	contents = parseFile("input")

	grid = dict()

	for line in contents:
		begin = line["begin"]
		end = line["end"]

		if(isVertical(begin, end)):
#			print("V: " + str(line))
			low = min(begin["y"], end["y"])
			high = max(begin["y"], end["y"])
			for j in range(low, high+1):
				incrementGrid(grid, begin["x"], j)
		elif(isHorizontal(begin, end)):
#			print("H: " + str(line))
			low = min(begin["x"], end["x"])
			high = max(begin["x"], end["x"])
			for j in range(low, high+1):
				incrementGrid(grid, j, begin["y"])
		else:
#			print("D: " + str(line))
			if begin["x"] < end["x"]:
				xDelta = 1
			else:
				xDelta = -1

			if begin["y"] < end["y"]:
				yDelta = 1
			else:
				yDelta = -1

			delta = { "x" : xDelta, "y" : yDelta }
			print(delta)

			start = begin
			while(start != end):
				incrementGrid(grid, start["x"], start["y"])
				start = addDelta(start, delta)
			incrementGrid(grid, end["x"], end["y"])


	count = 0;
	for k in grid:
		if grid[k] > 1:
			count += 1

	print(count)













main()
