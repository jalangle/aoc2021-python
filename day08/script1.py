#!python3

# Normally....
# 0: abcefg = 6
# 1: cf = 2
# 2: acdeg = 5
# 3: acdfg = 5
# 4: bcdf = 4
# 5: abdfg = 5
# 6: abdefg = 6
# 7: acf = 3
# 8: abcdefg = 7
# 9: abdcfg = 6

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			(inputs, outputs) = l.rstrip().split('|')
			item = dict()
			item["inputs"] = inputs.lstrip().split(' ')
			item["outputs"] = outputs.lstrip().split(' ')

			contents.append(item)
	return contents

def main():
	contents = parseFile("input")
#	pp.pprint(contents)
	digitCounts = list()
	for i in range(0,10):
		digitCounts.append(0)

	for row in contents:
		for digit in row["outputs"]:
			if(len(digit) == 2):
				digitCounts[1] += 1
			elif(len(digit) == 4):
				digitCounts[4] += 1
			elif(len(digit) == 3):
				digitCounts[7] += 1
			elif(len(digit) == 7):
				digitCounts[8] += 1

	print( sum(digitCounts))
	return 

main()