#!/home/ayushjain1144/anaconda3/bin/python
import sys
import math

test_vals = []

# We give test data as arguments to mapper.
for x in range(9):
	# argv starts from 1.
	test_vals.append(sys.argv[x+1])

# We get training examples from STDIN, one by one.
for lines in sys.stdin:
	ssum = 0.0
	lines = lines.strip()
	attrs = lines.split(',')
	for i in range(len(attrs)-1):
		if attrs[i]:
			ssum += (float(attrs[i]) - float(test_vals[i]))**2
	dist = math.sqrt(ssum)
	
	print(f"{attrs[-1]}\t{dist}")
