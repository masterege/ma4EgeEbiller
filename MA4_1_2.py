
"""
Solutions to module 4
Review date:
"""

student = "Ege Ebiller"
reviewer = "Aoping Lyu"

import math as m
import random as r
from functools import reduce

def sphere_volume(n, d):
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
    print(f"Approximation of volume in {d} dimensions: {volume_approx}")
    print(f"Exact volume in {d} dimensions: {exact_volume}")
    return volume_approx

# Exact volume of d-dimensional hypersphere using the formula
def hypersphere_exact(n, d):
    return (m.pi**(d/2)) / m.gamma(d/2 + 1)

def main():
    n = 100000
    d = 2
    sphere_volume(n, d)

if __name__ == '__main__':
	main()
