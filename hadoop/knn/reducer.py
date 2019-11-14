#!/usr/bin/python3
import sys

training_entries = []
# Keep a count of the labels.
counter = [0] * 7
estimated_val = 0.0
# We give the value of k as arguments to reducer.
k = int(sys.argv[1])

# Reducer takes the output of mapper from STDIN.
for lines in sys.stdin:
    lines = lines.strip()
    attrs = lines.split(',')
    training_entries.append(attrs)
# Sort the training entries in ascending order based on the calculated euclidean distance.
# Distance is the zeroth index in the training entry.
training_entries = sorted(training_entries)

# Check the k-nearest neighbors.
for i in range(k):
    counter[training_entries[i][1]-1] += 1

test_label = max(enumerate(counter), key=lambda entry: entry[1])[0]
print(test_label)
