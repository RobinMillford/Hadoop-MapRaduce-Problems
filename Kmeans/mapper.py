#!/usr/bin/env python

import sys
import os
import math

CENTROID_FILE_NAME = "centroid.txt"
SPLITTER = "\t| "

def read_centroids():
    centroids = []
    with open(CENTROID_FILE_NAME, 'r') as f:
        for line in f:
            centroid = float(line.strip().split(SPLITTER)[0])
            centroids.append(centroid)
    return centroids

def map():
    centroids = read_centroids()
    for line in sys.stdin:
        point = float(line.strip())
        min_distance = float('inf')
        nearest_centroid = None
        for centroid in centroids:
            distance = abs(centroid - point)
            if distance < min_distance:
                min_distance = distance
                nearest_centroid = centroid
        print(f"{nearest_centroid}\t{point}")

if __name__ == "__main__":
    map()

