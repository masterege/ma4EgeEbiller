
"""
Solutions to module 4
Review date:
"""

student = "Ege Ebiller"
reviewer = ""


import random as r
import math
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside_circle = 0
    points_inside = []
    points_outside = []
    # Random point generation
    for i in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        # Check if it is in the circle
        if x ** 2 + y ** 2 <= 1:
            inside_circle = inside_circle + 1
            points_inside.append((x, y)) # Append x and y as a tuple
        else:
            points_outside.append((x, y))
    # Approximate pi
    pi = 4 * inside_circle / n
    # Print results
    print(f"Points inside the circle: {inside_circle}")
    print(f"Approximation of π: {pi}")
    print(f"Builtin π: {math.pi}")

    # Plot the points
    inside_x, inside_y = zip(*points_inside)
    outside_x, outside_y = zip(*points_outside)

    plt.scatter(inside_x, inside_y, color='red', s=1)
    plt.scatter(outside_x, outside_y, color='blue', s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(f'C:\Users\egeeb\Python\CPII\MA4_files\monte_carlo_pi_{n}.png')
    plt.show()
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
