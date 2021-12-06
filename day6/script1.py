#!python3

import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

REPRODUCTION_RATE = 7
REPRODUCTION_MATURITY_RATE = 2

NUMBER_OF_DAYS = 80

def parseFile(path):
	"""Retrieve file contents"""
	contents = None
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			contents = [int(x) for x in l.split(",")]
	return contents

def main():
	lanternfishes = parseFile("input")

	for day in range(0,NUMBER_OF_DAYS):
		newToAdd = 0
		for i in range(0, len(lanternfishes)):
			lanternfishes[i] -= 1
			if(lanternfishes[i] < 0):
				lanternfishes[i] = REPRODUCTION_RATE - 1
				lanternfishes.append(REPRODUCTION_MATURITY_RATE + REPRODUCTION_RATE -1)
#		print("After " + str(day) + " days: " + str(lanternfishes))

	print("Count: " + str(len(lanternfishes)))
main()
