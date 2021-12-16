#!python3
import logging
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)

def slurpFile(path):
	"""Retrieve file contents"""
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def parse(line):
	""" """
	(command, value) = line.split(' ')
	return(command, int(value))

def func(path):
	contents = list(map(parse, slurpFile(path)))

	horiz = 0
	depth = 0
	aim = 0

	for c in contents:
		if(c[0] == "forward"):
			horiz += c[1]
			depth += (aim * c[1])
		elif(c[0] == "down"):
			aim += c[1]
		elif(c[0] == "up"):
			aim -= c[1]

	logging.debug("Horizontal Postition: " + str(horiz))
	logging.debug("Depth: " + str(depth))
	logging.debug("H*D: " + str(horiz * depth))
	return horiz * depth

class TestDay2Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 900)

	def test_inputdata(self):
		self.assertEqual(func('input'), 1604592846)

if __name__ == '__main__':
	unittest.main()