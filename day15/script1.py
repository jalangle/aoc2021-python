#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

import networkx as nx

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			vals = list()
			for c in l.rstrip():
				vals.append(int(c))
			contents.append(vals)
	return contents

def GetCost(grid, r, c):
	if r < 0:
		return None
	if r >= len(grid):
		return None
	if c < 0:
		return None
	if c >= len(grid[0]):
		return None
	return grid[r][c]
	
def GetName(r, c):
	return str(r) + "," + str(c)

def GetKey(r_from, c_from, r_to, c_to):
	return GetName(r_from, c_from) + "-" + GetName(r_to, c_to)

def AddEdge(grid, graph, costs, r_from, c_from, r_to, c_to):
	fromName = GetName(r_from, c_from)
	toName = GetName(r_to, c_to)

	cost = GetCost(grid, r_to, c_to)
	if(cost):
		costs[fromName + "-" + toName] = cost
		graph.add_edge(fromName, toName, weight = cost)	

def func(path):
	grid = parseFile(path)
#	pp.pprint(grid)
#	print("-" * 40)
	g = nx.DiGraph()

	costs = dict()
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			name = GetName(r, c)

			AddEdge(grid, g, costs, r, c, r-1, c)
			AddEdge(grid, g, costs, r, c, r+1, c)
			AddEdge(grid, g, costs, r, c, r, c-1)
			AddEdge(grid, g, costs, r, c, r, c+1)

#	print("-" * 40)

	path = nx.shortest_path(g, GetName(0, 0), GetName(len(grid)-1,len(grid[0]) -1), weight='weight')

	cost = 0
	for i in range(len(path) - 1):
		segment = path[i:i+2]
		key = segment[0] + "-" + segment[1]
#		print(key)
#		print(key + " => " + str(costs[key]))
		cost += costs[key]

	logging.debug(cost)
	return cost

class TestDay15Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 40)

	def test_inputdata(self):
		self.assertEqual(func('input'), 589)

if __name__ == '__main__':
	unittest.main()