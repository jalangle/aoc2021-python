#!python3

import logging
logging.basicConfig(filemode='w', level=logging.INFO)

import pprint
pp = pprint.PrettyPrinter(indent=4)

import networkx as nx
import matplotlib.pyplot as plt

from copy import deepcopy

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

def printGrid(grid):
	for r in range(len(grid)):
		strs = list(map(str, grid[r]))
		print("".join(strs))

def incrementCell(grid, r, c):
	grid[r][c] += 1
	if(grid[r][c] > 9):
		grid[r][c] = 1

def incrementRow(grid, r):
	for c in range(0, len(grid[r])):
		incrementCell(grid, r, c)

def incrementGrid(grid):
	for r in range(0, len(grid)):
		incrementRow(grid, r)

def main():
	initialGrid = parseFile("input")

	grid = list()
	p1 = deepcopy(initialGrid)
	grid.extend(p1)

	p2 = deepcopy(p1)
	incrementGrid(p2)
	grid.extend(p2)

	p3 = deepcopy(p2)
	incrementGrid(p3)
	grid.extend(p3)

	p4 = deepcopy(p3)
	incrementGrid(p4)
	grid.extend(p4)

	p5 = deepcopy(p4)
	incrementGrid(p5)
	grid.extend(p5)

	expanded = list()

	# expand right
	for r in range(0, len(grid)):
		initialRow = grid[r]
		expandedRow = deepcopy(initialRow)
		for i in range(4):
			for c in range(len(initialRow)):
				initialRow[c] += 1
				if(initialRow[c] > 9):
					initialRow[c] = 1
			expandedRow.extend(initialRow)
		expanded.append(expandedRow)

#	print("1. expanded grid dimensions: " + str(len(expanded)) + "," + str(len(expanded[0])))	
	grid = expanded

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

	#nx.draw(g,with_labels=True)
	#plt.show()
	path = nx.shortest_path(g, GetName(0, 0), GetName(len(grid)-1,len(grid[0]) -1), weight='weight')

	cost = 0
	for i in range(len(path) - 1):
		segment = path[i:i+2]
		key = segment[0] + "-" + segment[1]
#		print(key)
#		print(key + " => " + str(costs[key]))
		cost += costs[key]

	print(cost)
	return

main()