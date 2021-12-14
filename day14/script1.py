#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
pp = pprint.PrettyPrinter(indent=4)

STEPS = 10

def parseFile(path):
	initial = ""
	insertions = dict()
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			if(initial == ""):
				initial = l
			elif(l != ""):
				(pair, insertion) = l.split(" -> ")
				insertions[pair] = insertion
	return (initial, insertions)

def insertAt(strOriginal, strToInsert, pos):
	return strOriginal[:pos] + strToInsert + strOriginal[pos:]

def main():
	(polymer, insertions) = parseFile("input")

	for s in range(0, STEPS):
		print("STEP " + str(s))
		for i in range(len(polymer)-2, -1, -1):
			#print("Pos: " + str(i))
			pair = polymer[i:i+2]
			#print("  Pair: " + pair)
			#print("  Before: " + polymer)
			if(pair in insertions):
				#print("  Insertion: " + insertions[pair])
				polymer = insertAt(polymer, insertions[pair], i + 1)
			#print("  After: " + polymer)
			#print("-" * 40)

	print("-" * 40)
	counts = dict()
	for c in polymer:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1

	pp.pprint(counts)

	maxCount = 0
	minCount = 1000000000000000000000000
	for c in counts:
		if counts[c] > maxCount:
			maxCount = counts[c]
		elif counts[c] < minCount:
			minCount = counts[c]

	print(str(maxCount - minCount))

	return

main()