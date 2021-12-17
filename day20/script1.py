#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.WARN)
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def func(path):
	contents = parseFile(path)
	logging.debug(contents)
	return 0

class TestDay17Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 0)

	def test_inputdata(self):
		self.assertEqual(func('input'), 0)

if __name__ == '__main__':
	unittest.main()
