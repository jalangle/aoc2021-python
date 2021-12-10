#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def main():
	contents = parseFile("test")
	print(contents)
	return

main()