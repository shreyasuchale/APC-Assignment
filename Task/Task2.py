# 2.Write a program to develope a system that manages the positions of points in a 2D plane.
# The position of each point is represented as a tuple of two values: (x, y). Write a program that:
# ●	Takes a list of points as input.
# ●	Calculates the distance between two given points.
# ●	Finds the point that is farthest from the origin (0, 0).

# Tasks:
# ●	Use tuples to represent the coordinates of each point.
# ●	Implement a function to calculate the Euclidean distance between two points using their tuple representations.
# ●	Implement a function to find the farthest point from the origin

import math

def distance(p1, p2):
    d = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return d

def farthest_point(points):
    origin = (0, 0)

    farthest = points[0]
    max_distance = distance(origin, farthest)

    for point in points:
        d = distance(origin, point)

        if d > max_distance:
            max_distance = d
            farthest = point

    print("Farthest Point :", farthest)
    print("Distance from Origin :", max_distance)

points = []

n = int(input("Enter Number of Points: "))

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    points.append((x, y))

print("\nPoints =", points)

i = int(input("\nEnter First Point Index: "))
j = int(input("Enter Second Point Index: "))

d = distance(points[i], points[j])

print("Distance Between Points =", d)
farthest_point(points)