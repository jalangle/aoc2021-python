#!python3

prev = -1
increase = 0
with open("input", 'r') as f:
	for l in f:
		i = int(l)
		if i > prev:
			if prev != -1:
				increase+=1
		prev = i
	f.close()

print(increase)