#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)


def parseFile(path):
	return "Hello, World"

def main():
	contents = parseFile("test")
	print(contents)
	return

main()