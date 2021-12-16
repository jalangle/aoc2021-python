#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.INFO)
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	heightmap = list()
	with open(path, 'r') as f:
		for l in f:
			row = list()
			l = l.rstrip()
			for c in l:
				row.append(int(c))
			heightmap.append(row)
		f.close()
	return heightmap

def get_north(data, x, y):
	count_rows = len(data)
	if( x == 0 ): #can't go north so return something larger than it can be
		return 1000000
	return data[x-1][y]

def get_south(data, x, y):
	count_rows = len(data)
	if( x == count_rows - 1): #can't go south so return something larger than it can be
		return 1000000
	return data[x+1][y]

def get_east(data, x, y):
	count_cols = len(data[0])
	if( y == count_cols -1 ): #can't go east so return something larger than it can be
		return 1000000
	return data[x][y+1]

def get_west(data, x, y):
	count_cols = len(data[0])
	if( y == 0): #can't go east so return something larger than it can be
		return 1000000
	return data[x][y-1]

def explore(heightmap, explored_points, x, y):
	if (x,y) in explored_points:
		return set()

	if(heightmap[x][y] >= 9):
		return set()

	explored_points.add((x,y))

	if(x != 0): # explore north
		explored_points.update(explore(heightmap, explored_points, x-1, y))
	if(x != len(heightmap) - 1): # explore south
		explored_points.update(explore(heightmap, explored_points, x+1, y))
	if(y != 0): # explore west
		explored_points.update(explore(heightmap, explored_points, x, y-1))
	if(y != len(heightmap[0]) - 1): # explore east
		explored_points.update(explore(heightmap, explored_points, x, y+1))

	return explored_points

def func(path):
	heightmap = parseFile(path)
#	pp.pprint(heightmap)
	count_rows = len(heightmap)
	count_cols = len(heightmap[0])

	risklevel = 0
	basins = list()
	for i in range(0, count_rows):
		for j in range(0, count_cols):
			val = heightmap[i][j]
			n = get_north(heightmap, i, j)
			s = get_south(heightmap, i, j)
			e = get_east(heightmap, i, j)
			w = get_west(heightmap, i, j)

			if val < n and val < s and val < e and val < w:
				basins.append( explore(heightmap, set(), i, j) )

	basins.sort(key = len, reverse=True)
	sizes = [len(x) for x in basins[0:3]]

	logging.debug(str(sizes[0] * sizes[1] * sizes[2]))
	return sizes[0] * sizes[1] * sizes[2]

class TestDay9Part2(unittest.TestCase):

	def test_testdata(self):
		self.assertEqual(func('test'), 1134)

	def test_inputdata(self):
		self.assertEqual(func('input'), 1558722)

if __name__ == '__main__':
	unittest.main()