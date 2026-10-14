

import math


# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Function to find the point farthest from the origin
def farthest_from_origin(points):
    farthest_point = points[0]
    max_distance = calculate_distance(farthest_point, (0, 0))

    for point in points:
        distance = calculate_distance(point, (0, 0))

        if distance > max_distance:
            max_distance = distance
            farthest_point = point

    return farthest_point, max_distance


# Take points as input
points = []

n = int(input("Enter the number of points: "))

for i in range(n):
    x = float(input(f"Enter x-coordinate of point {i + 1}: "))
    y = float(input(f"Enter y-coordinate of point {i + 1}: "))

    point = (x, y)
    points.append(point)


# Display the points
print("\nPoints entered:")
for point in points:
    print(point)


# Take two points for distance calculation
print("\nEnter the index of two points to calculate distance.")
print("Point numbers start from 1.")

p1 = int(input("Enter first point number: "))
p2 = int(input("Enter second point number: "))

point1 = points[p1 - 1]
point2 = points[p2 - 1]

distance = calculate_distance(point1, point2)

print("Distance between", point1, "and", point2, "=", round(distance, 2))


# Find the farthest point from origin
farthest_point, max_distance = farthest_from_origin(points)

print("\nPoint farthest from origin:", farthest_point)
print("Distance from origin:", round(max_distance, 2))