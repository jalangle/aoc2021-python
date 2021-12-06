#!python3

import logging

logging.basicConfig(filemode='w', level=logging.DEBUG)

def parseFile(path):
	"""Retrieve file contents"""
	contents = None
	with open(path, 'r') as f:
		for l in f:
			l = l.rstrip()
			contents = l.split(",")
	return contents

def main():
	contents = parseFile("test")
	print(contents)

main()
