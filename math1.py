#Write a Python program to calculate the area of regular polygon.

import math

num_sides = int(input("Enter number sides:"))
side_length = float(input("Enter the length of side:"))

area_of_polygon = (num_sides * side_length**2)/(4*math.tan(math.pi/num_sides))

print(f"The area of the polygon is: {area_of_polygon}")

