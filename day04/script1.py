#!python3
from itertools import islice
import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

def parseFile(path):
	"""Retrieve file contents"""
	contents = list()
	firstline = True
	drawOrder = list()
	cards = list()
	card = list()
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			if(firstline):
				drawOrder = [int(x) for x in l.split(',')]
				firstline = False
			elif(len(l) == 0):
				if(len(card) > 0):
					cards.append(card)
				card = list()
			else:
				values = [(int(x), False) for x in l.split(' ') if x != ""]
				card.append(values)
	cards.append(card)

	return (drawOrder, cards)

def isBingo(card):
	for r in card:
		valuesAtIndex = [x[1] for x in r]
		if(all(valuesAtIndex)):
			return True


	for i in range(0, 5):
		valuesAtIndex = [row[i][1] for row in card]
		if(all(valuesAtIndex)):
			return True

	return False

def markCard(value, card):
	for r in range(0,5):
		for c in range(0,5):
			if(card[r][c][0] == value):
				card[r][c] = (value, True)

	return isBingo(card)

def score(value, card):
	total = 0;
	for l in card:
		for r in l:
			if(r[1] == False):
				total += r[0]

	return value * total

def printCard(card):
	print("-----------")
	for r in card:
		print(r)

def main():
	(drawOrder, cards) = parseFile("input")

	for value in drawOrder:
		for card in cards: 
			bingo = markCard(value, card)
			if(bingo):
				s = score(value, card)
				printCard(card)
				print(s)
				return

main()