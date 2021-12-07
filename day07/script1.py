#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)


def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			values = l.rstrip().split(',')
			for x in values:
				contents.append(int(x))
	return contents

def costToMoveFrom(f, t):
	return abs(f - t)

def main():
	crabPositions = parseFile("input")
	print(crabPositions)

	maxPos = max(crabPositions)

	posCosts = list()
	for pos in range(0, maxPos):
		posCosts.append(0)
		for crab in crabPositions:
			posCosts[pos] += costToMoveFrom(crab, pos)

	print(posCosts)
	print(str(min(posCosts)))
	return

main()