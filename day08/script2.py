#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
pp = pprint.PrettyPrinter(indent=4)

def normalizeWire(pattern):
	s = ''.join(sorted(pattern))
	return s

def normalizeWires(wires):
	for i in range(0, len(wires)):
		wires[i] = normalizeWire(wires[i])
	return wires

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			(inputs, outputs) = l.rstrip().split(" | ")
			item = dict()
			item["inputs"] = normalizeWires(inputs.lstrip().split(' '))
			item["outputs"] = normalizeWires(outputs.lstrip().split(' '))

			contents.append(item)
	return contents

def containsWiresOf(x, y):
	if len(x) < len(y):
		return False
	for c in y:
		if x.find(c) == -1:
			return False
	return True

def areEqualWires(x, y):
	if len(x) != len(y):
		return False
	for c in y:
		if x.find(c) == -1:
			return False
	return True

# 0: abcefg = 6
def deduceDisplays(uniquePatterns):
	displayNumbers = ["" for x in range(0,10)]
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# print("-" * 20 + " 1,4,7,8 " + "-" * 20)

	# extract the easy ones
	for i in range(0, len(uniquePatterns)):
		if(uniquePatterns[i] == ""):
			continue
		if(len(uniquePatterns[i]) == 2):
			displayNumbers[1] = uniquePatterns[i]
			uniquePatterns[i] = ""
		elif(len(uniquePatterns[i]) == 3):
			displayNumbers[7] = uniquePatterns[i]
			uniquePatterns[i] = ""
		elif(len(uniquePatterns[i]) == 4):
			displayNumbers[4] = uniquePatterns[i]
			uniquePatterns[i] = ""
		elif(len(uniquePatterns[i]) == 7):
			displayNumbers[8] = uniquePatterns[i]
			uniquePatterns[i] = ""

	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# the number 3 is the only 5 bit display that has both the bits of 1
	# print("-" * 20 + " 3 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 5):
			if containsWiresOf(uniquePatterns[i], displayNumbers[1]):
				displayNumbers[3] = uniquePatterns[i]
				uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)


	# the number 9 is the only 6 bit display that has all the same bits as 4
	# print("-" * 20 + " 9 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 6):
			if containsWiresOf(uniquePatterns[i], displayNumbers[4]):
				displayNumbers[9] = uniquePatterns[i]
				uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# the number 5 is the only remanining 5 character element that is subsumed by the 6 char display of 9
	# print("-" * 20 + " 5 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 5):
			if containsWiresOf(displayNumbers[9], uniquePatterns[i]):
				displayNumbers[5] = uniquePatterns[i]
				uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# the number 2 is the only remaining 5 character left
	# print("-" * 20 + " 2 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 5):
			displayNumbers[2] = uniquePatterns[i]
			uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# the number 6 overlaps with 5
	# print("-" * 20 + " 6 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 6):
			if containsWiresOf(uniquePatterns[i], displayNumbers[5]):
				displayNumbers[6] = uniquePatterns[i]
				uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	# 0 is the only remaining character
	# print("-" * 20 + " 0 " + "-" * 20)
	for i in range(0, len(uniquePatterns)):
		if(len(uniquePatterns[i]) == 6):
			displayNumbers[0] = uniquePatterns[i]
			uniquePatterns[i] = ""
	#pp.pprint(displayNumbers)
	#pp.pprint(uniquePatterns)

	return displayNumbers


def main():
	contents = parseFile("input")

	total = 0
	for i in range(0,len(contents)):
		allWirePatterns = list()
		allWirePatterns.extend(contents[i]["inputs"])
		allWirePatterns.extend(contents[i]["outputs"])
		uniquePatterns = set(allWirePatterns)
#		pp.pprint(uniquePatterns)
#		print("=" * 20)
		displayNumbers = deduceDisplays(list(uniquePatterns))
		pp.pprint(displayNumbers)
		outputValue = 0;

		for idx in range(0, len(contents[i]["outputs"])):
			powerOfTen = pow(10, (len(contents[i]["outputs"]) - idx - 1))
			for value in range(0,10):
				if (areEqualWires(contents[i]["outputs"][idx], displayNumbers[value])):
					number = value * powerOfTen
					print("Digit " + str(idx) + " = " + str(value) + " => " + str(number))
					outputValue += number
		print("OUTPUT: " + str(outputValue))
		total += outputValue
	print("Total: " + str(total))

	return 

main()