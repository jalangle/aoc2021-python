#!python3

import unittest

def func(path):
	prev = -1
	increase = 0
	with open(path, 'r') as f:
		for l in f:
			i = int(l)
			if i > prev:
				if prev != -1:
					increase+=1
			prev = i
		f.close()

	return increase

class TestDay1Part1(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 7)

	def test_inputdata(self):
		self.assertEqual(func('input'), 1665)


if __name__ == '__main__':
	unittest.main()