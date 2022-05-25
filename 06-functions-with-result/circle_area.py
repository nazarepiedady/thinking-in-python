import area
import distance


def calculate_circle_area(xc, yc, xp, yp):
    radius = distance.calculate_distance(xc, yc, xp, yp)
    circle_area = area.calculate_area(radius)
