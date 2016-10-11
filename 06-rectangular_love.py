#!/usr/bin/python2

import itertools
import sys


def find_intersection(r1, r2):
    # Check if no intersections
    # Check for X axis
    if r1['left_x'] + r1['width'] <= r2['left_x']:
        return {}
    if r2['left_x'] + r2['width'] <= r1['left_x']:
        return {}

    # Check for Y axis
    if r1['bottom_y'] + r1['height'] <= r2['bottom_y']:
        return {}
    if r2['bottom_y'] + r2['height'] <= r1['bottom_y']:
        return {}

    r1x = [r1['left_x'], r1['left_x'] + r1['width']]
    r1y = [r1['bottom_y'], r1['bottom_y'] + r1['height']]
    r2x = [r2['left_x'], r2['left_x'] + r2['width']]
    r2y = [r2['bottom_y'], r2['bottom_y'] + r2['height']]

    x_pts = sorted(r1x + r2x)
    y_pts = sorted(r1y + r2y)

    return {
        'left_x': x_pts[1:-1][0],
        'bottom_y': y_pts[1:-1][0],
        'width': x_pts[1:-1][1] - x_pts[1:-1][0],
        'height': y_pts[1:-1][1] - y_pts[1:-1][0],
    }

if __name__ == "__main__":
    rect1 = {
        'left_x': 1,
        'bottom_y': 5,
        'width': 10,
        'height': 4,
    }

    rect2 = {
        'left_x': 6,
        'bottom_y': 7,
        'width': 1,
        'height': 1,
    }
    print find_intersection(rect1, rect2)
