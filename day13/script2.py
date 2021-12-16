#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

from enum import Enum

class FoldDirection(Enum):
	Up = 1
	Left = 2

class Point:
	def __init__(self, str):
		(col,row) = str.rstrip().split(',')
		self.row = int(row)
		self.col = int(col)

	def __str__(self):
		return "(" + str(self.col) + "," + str(self.row) + ")"

	def __repr__(self):
		return str(self)

	def __lt__(self, other):
		if(self.row < other.row):
			return True
		if(self.row > other.row):
			return False
		return self.col < other.col

	def __eq__(self, other):
		return (self.row == other.row and self.col == other.col)

class Instruction:
	def __init__(self, str):
		(direction,value) = str.rstrip().split('=')
		if direction == "fold along x":
			self.direction = FoldDirection.Left
		else:
			self.direction = FoldDirection.Up
		self.value = int(value)

	def __str__(self):
		return "(" + str(self.direction) + "," + str(self.value) + ")"

	def __repr__(self):
		return str(self)

def parseFile(path):
	points = list()
	instructions = list()

	onInstructions = False
	with open(path, 'r') as f:
		for l in f:
			if onInstructions:
				instructions.append(Instruction(l))
				pass
			elif l.rstrip() == "":
				onInstructions = True
			else:
				points.append(Point(l))
				
	return (points, instructions)

def maxRows(points):
	return max([pt.row for pt in points])

def maxCols(points):
	return max([pt.col for pt in points])

def printGrid(points):
	maxRow = maxRows(points) + 1
	maxCol = maxCols(points) + 1

	grid = list()
	for x in range(0, maxCol):
		row = list()
		for y in range(0, maxRow):
			row.append(' ')
		grid.append(row)

	count = 0
	for pt in points:
		if(grid[pt.col][pt.row] != '#'):
			count += 1
		grid[pt.col][pt.row] = '#'
#	print("-" * 40)
#	pp.pprint(grid)

	for i in range(0, maxRow):
		row = ""
		for col in grid:
			row += col[i]
#		print(row)

	return count

def func(path):
	(points, instructions) = parseFile(path)

	for instruction in instructions:
		if(instruction.direction == FoldDirection.Up):
			topSize = instruction.value - 1
			bottomSize = maxRows(points) - instruction.value - 1
#			print ("TS: " + str(topSize) + " - BS: " + str(bottomSize))

			for i in range(0, len(points)):
				if(points[i].row > instruction.value):
					diff = points[i].row - instruction.value
					newRow = instruction.value - diff
					points[i].row = newRow
				else:
					pass
		else:
			for i in range(0, len(points)):
				if(points[i].col > instruction.value):
					diff = points[i].col - instruction.value
					newCol = instruction.value - diff
					points[i].col = newCol

	count = printGrid(points)
	return count

class TestDay13Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 16)

	def test_inputdata(self):
		self.assertEqual(func('input'), 100)

if __name__ == '__main__':
	unittest.main()