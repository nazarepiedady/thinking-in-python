# import area
# import distance


# def calculate_circle_area(xc, yc, xp, yp):
#     radius = distance.calculate_distance(xc, yc, xp, yp)
#     circle_area = area.calculate_area(radius)
#     return circle_area

from area import calculate_area
from distance import calculate_distance


def calculate_circle_area(xc, yc, xp, yp):
    return calculate_area(calculate_distance(xc, yc, xp, yp))
