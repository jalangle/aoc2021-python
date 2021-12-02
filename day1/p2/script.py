#!python3
import collections
import logging

logging.basicConfig(filename='script.log', filemode='w', level=logging.DEBUG)

WINDOWSIZE = 3

increase = 0
prev = -1
window = collections.deque(maxlen=WINDOWSIZE)

with open("input", 'r') as f:
	for l in f:
		i = int(l)
		window.append(i)
		if(len(window) < WINDOWSIZE):
			continue
		logging.debug(repr(window))
		windowSize = sum(window)
		if windowSize > prev:
			if prev != -1 and len(window) == WINDOWSIZE:
				increase+=1
		prev = windowSize

	f.close()

print(increase)