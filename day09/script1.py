#!python3

import logging
logging.basicConfig(filemode='w', level=logging.DEBUG)

import pprint
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


def main():
	heightmap = parseFile("input")
#	pp.pprint(heightmap)
	count_rows = len(heightmap)
	count_cols = len(heightmap[0])

	risklevel = 0
	for i in range(0, count_rows):
		for j in range(0, count_cols):
			val = heightmap[i][j]
			n = get_north(heightmap, i, j)
			s = get_south(heightmap, i, j)
			e = get_east(heightmap, i, j)
			w = get_west(heightmap, i, j)

			if val < n and val < s and val < e and val < w:
#				print("(" + str(i) + "," + str(j) + ")")
				risklevel += (1 + val)


	print(risklevel)
	return

main()