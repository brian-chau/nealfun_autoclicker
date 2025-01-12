import pyautogui as py
import math
import sys

def circle_points(center_x: int, center_y: int, radius: int, num_points: int) -> list:
    """Calculates x and y positions of points on a circle.

    Args:
    center_x: The x-coordinate of the circle's center.
    center_y: The y-coordinate of the circle's center.
    radius: The radius of the circle.
    num_points: The number of points to generate.

    Returns:
    A list of tuples, each containing the x and y coordinates of a point.
    """

    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        x,y = int(x), int(y)
        points.append((x, y))
    return points

# Example usage
num_points = 100
center = (480, 540)
radius = 200

points = circle_points(center[0], center[1], radius, num_points)
py.moveTo( points[0][0], points[0][1] )
py.mouseDown()
py.PAUSE = 0.01


for pos in points:
    py.moveTo(pos[0], pos[1])

py.mouseUp()