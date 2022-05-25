import math

def calculate_distance(x1, y1, x2, y2):
    horizontal_distance = x2 - x1
    vertical_distance = y2 - y1
    squared_distance = horizontal_distance ** 2 + vertical_distance ** 2
    distance = math.sqrt(squared_distance)
    return distance
