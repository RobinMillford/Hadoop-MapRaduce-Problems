#!/usr/bin/env python

import sys

def reduce():
    current_centroid = None
    current_points = []

    for line in sys.stdin:
        centroid, point = line.strip().split('\t')
        point = float(point)
        
        if centroid != current_centroid:
            if current_centroid:
                new_center = sum(current_points) / len(current_points)
                print(f"{new_center}\t{' '.join(map(str, current_points))}")
            current_centroid = centroid
            current_points = []
        
        current_points.append(point)

    if current_centroid:
        new_center = sum(current_points) / len(current_points)
        print(f"{new_center}\t{' '.join(map(str, current_points))}")

if __name__ == "__main__":
    reduce()

