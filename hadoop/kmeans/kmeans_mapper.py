#!/usr/bin/env python3 


# Manage the fpath: file path of centroid

import sys
import math

# take centroids from file passed in fpath
# There would be a file in which we will keep updating centroids
# This function just parses that
def getCentroids(fpath):
    centroids = []

    for line in open(fpath).readlines():
        if line:
            centroids.append(list(map(float, line.strip().split(','))))
    return centroids

def get_distance(x1, x2):
    """Returns Eucledian Distance"""

    assert(len(x1) == len(x2))
    ssum = 0
    for i in range(len(x1)):
        if x1[i]:
            ssum += (float(x1[i]) - float(x2[i]))**2
    dist = math.sqrt(ssum)   

    return dist

def map_line(line, centroids):

    #centroids = getCentroids(fpath)

    #for line in sys.stdin:

    data_point = list(map(float, line.strip().split(',')))
    min_dist = float('Inf')
    idx = -1

    for i, centroid in enumerate(centroids):
        current_distance = get_distance(data_point, centroid)

        if current_distance < min_dist:
            min_dist = current_distance
            idx = i

    data_tuple = (data_point, 1)
    # Returns index of centroid and the data point tuple (refer to the research paper in the readme of our github)
    # print(f"{idx}\t{data_tuple}") 
    print(f"{idx}\t{str(data_tuple)}")           

        


def kmeans_mapper(fpath):
    centroids = getCentroids(fpath)
    for line in sys.stdin:
        map_line(line, centroids)

kmeans_mapper("centroids.txt")        






 
