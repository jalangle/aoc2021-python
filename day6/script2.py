#!python3

import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

REPRODUCTION_RATE = 7
REPRODUCTION_MATURITY_RATE = 2

NUMBER_OF_DAYS = 256

def newFish(interval, count):
	return { "count" : count, "interval" : interval }

def parseFile(path):
	"""Retrieve file contents"""
	contents = None
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			intervals = [int(x) for x in l.split(",")]
			contents = [newFish(x, 1) for x in intervals]
	return contents

def main():
	lanternfishes = parseFile("input")

	for day in range(0,NUMBER_OF_DAYS):
		numberToAdd = 0
		for i in range(0, len(lanternfishes)):
			lanternfishes[i]["interval"] -= 1
			if(lanternfishes[i]["interval"] < 0):
				lanternfishes[i]["interval"] = REPRODUCTION_RATE - 1
				numberToAdd += lanternfishes[i]["count"]

		if(numberToAdd > 0):
			lanternfishes.append(newFish(REPRODUCTION_MATURITY_RATE + REPRODUCTION_RATE - 1, count=numberToAdd))

	count = 0
	for f in lanternfishes:
		count += f["count"]

	print("Count: " + str(count))

main()
