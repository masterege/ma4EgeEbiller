
"""
Solutions to module 4
Review date:
"""

student = "Ege Ebiller"
reviewer = ""

import math as m
import statistics
import random as r
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from time import perf_counter as pc

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    # Generate random points in d-dimensional space
    generate_point = lambda d: [r.uniform(-1, 1) for _ in range(d)]
    # Generate n points
    points = (generate_point(d) for _ in range(n))  # Using a generator for efficiency
    # Check if the point is inside the hypersphere using map and reduce
    inside_hypersphere = lambda point: reduce(lambda acc, x: acc + x, map(lambda x: x**2, point), 0) <= 1
    # Use filter to keep only the points inside the hypersphere
    points_inside = list(filter(inside_hypersphere, points))
    # Count how many are inside the hypersphere
    points_count = len(points_inside)
    # Approximate volume: V ≈ (2^d) * (points_inside / total_points)
    volume_approx = (2**d) * points_count / n
    # Calculate the exact volume for comparison
    exact_volume = hypersphere_exact(n, d)
    #print(f"Approximation of volume in {d} dimensions: {volume_approx}")
    #print(f"Exact volume in {d} dimensions: {exact_volume}")
    return volume_approx

def hypersphere_exact(n,d):
    return (m.pi**(d/2)) / m.gamma(d/2 + 1)

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    N = [n] * np
    D = [d] * np
    # Using ProcessPoolExecutor to parallelize the calls
    with ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, N, D))
    # Add up results from all parallel executions
    print(results)
    print((sum(results)) / np)
    return (sum(results)) / np # Average volume approximation

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, np):
    D = np * [d]
    process_chunk = [n // np for _ in range(np)]
    # Divide n into np segments for parallel processing
    with ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, process_chunk, D))
    # Added up results
    volume_approx = sum(results) / np
    return volume_approx

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 8

    for y in range (10):
        sphere_volume(n,d)
    
    sphere_volume_parallel1(n,d,np)

if __name__ == '__main__':
	main()
