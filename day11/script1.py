#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			line = list()
			for c in l.rstrip():
				line.append(int(c))
			contents.append(line)
	return contents

def printSep(label):
	print("-" * 20 + " " + label + " " + "-" * 20)

def increaseEnergy(octopodes):
	for x in range(0, len(octopodes)):
		for y in range(0, len(octopodes[0])):
			octopodes[x][y] += 1
	return octopodes

def resetFlashed(octopodes):
	flashed = 0
	for x in range(0, len(octopodes)):
		for y in range(0, len(octopodes[0])):
			if(octopodes[x][y] > 9):
				flashed += 1
				octopodes[x][y] = 0
	return flashed

def increaseNeighbor(octopodes, x, y, hasFlashed):
	if(x < 0):
		return
	if(x >= len(octopodes)):
		return
	if(y < 0):
		return
	if(y >= len(octopodes[0])):
		return
	octopodes[x][y] += 1
	if(octopodes[x][y] > 9):
		#print("Chain: " + strPt(x,y))
		flashOctopode(octopodes, x, y, hasFlashed)
		pass

def strPt(x, y):
	return "(" + str(x) + "," + str(y) + ")"

def flashOctopode(octopodes, x, y, hasFlashed):
	if (x,y) in hasFlashed:
		return

	hasFlashed.add((x,y))
	increaseNeighbor(octopodes, x-1, y-1, hasFlashed)
	increaseNeighbor(octopodes, x-1, y, hasFlashed)
	increaseNeighbor(octopodes, x-1, y+1, hasFlashed)
	increaseNeighbor(octopodes, x, y-1, hasFlashed)
	increaseNeighbor(octopodes, x, y+1, hasFlashed)
	increaseNeighbor(octopodes, x+1, y-1, hasFlashed)
	increaseNeighbor(octopodes, x+1, y, hasFlashed)
	increaseNeighbor(octopodes, x+1, y+1, hasFlashed)

def flashOctopodes(octopodes):
	hasFlashed = set()
	for x in range(0, len(octopodes)):
		for y in range(0, len(octopodes[0])):
			if(octopodes[x][y] > 9 and (x,y) not in hasFlashed):
				#print("Origin: " + strPt(x,y))
				#print("Flashed: " + str(hasFlashed))
				flashOctopode(octopodes, x, y, hasFlashed)
	return len(hasFlashed)

def main():
	octopodes = parseFile("input")
	#printSep("Initial")
	#pp.pprint(octopodes)

	flashes = 0
	days = 100
	for step in range(0,days):
		increaseEnergy(octopodes)
		flashes += flashOctopodes(octopodes)

		resetFlashed(octopodes)
		#printSep("After day " + str(step + 1))

		#pp.pprint(octopodes)

	#printSep("Done")
	print("Flashes: " + str(flashes))

	return

main()