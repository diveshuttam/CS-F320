#!/home/ayushjain1144/anaconda3/bin/python
import sys
import math

def map_line(line,testvals):
	ssum = 0.0
	line = line.strip()
	attrs = line.split(',')
	for i in range(len(attrs)-1):
		if attrs[i]:
			ssum += (float(attrs[i]) - float(test_vals[i]))**2
	dist = math.sqrt(ssum)
	return attrs[-1],dist

if __name__ == "__main__":
	test_vals = []
	# We give test data as arguments to mapper.
	for x in range(9):
		# argv starts from 1.
		test_vals.append(sys.argv[x+1])

	# We get training examples from STDIN, one by one.
	for line in sys.stdin:
		key,dist=map_line(line,test_vals)
		print(f"{key}\t{dist}")

