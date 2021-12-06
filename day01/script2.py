#!python3
from itertools import islice
import logging

logging.basicConfig(filename='script.log', filemode='w', level=logging.DEBUG)

WINDOWSIZE = 3

def slurpFile(path):
	"""Retrieve file contents"""
	contents = list()
	with open("input", 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

# window() definition taken from Python docs https://docs.python.org/release/2.3.5/lib/itertools-example.html
def window(seq, n=3):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def main():
	increase = 0
	prev = -1

	contents = list(map(int, slurpFile("input")))

	for w in window(contents, n=WINDOWSIZE):
		logging.debug(repr(w))
		windowSize = sum(w)
		if prev == -1:
			pass #do nothing.  Its the first iteration.
		elif windowSize > prev:
			increase+=1
		prev = windowSize

	print(increase)

main()
